#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Test YAML files."""


from __future__ import division

import collections
import copy
import logging
import os

from openfisca_core import conv, periods, scenarios
from openfisca_core.tools import assert_near
import numpy as np
import yaml

from openfisca_senegal import CountryTaxBenefitSystem as SenegalTBS
tax_benefit_system = SenegalTBS()

log = logging.getLogger(__name__)

options_by_dir = collections.OrderedDict()

# YAML configuration


class folded_unicode(unicode):
    pass


class literal_unicode(unicode):
    pass


def dict_constructor(loader, node):
    return collections.OrderedDict(loader.construct_pairs(node))


yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, dict_constructor)

yaml.add_representer(collections.OrderedDict, lambda dumper, data: dumper.represent_dict(
    (copy.deepcopy(key), value)
    for key, value in data.iteritems()
    ))
yaml.add_representer(dict, lambda dumper, data: dumper.represent_dict(
    (copy.deepcopy(key), value)
    for key, value in data.iteritems()
    ))
yaml.add_representer(folded_unicode, lambda dumper, data: dumper.represent_scalar(u'tag:yaml.org,2002:str',
    data, style='>'))
yaml.add_representer(literal_unicode, lambda dumper, data: dumper.represent_scalar(u'tag:yaml.org,2002:str',
    data, style='|'))
yaml.add_representer(np.ndarray, lambda dumper, data: dumper.represent_list(data.tolist()))
yaml.add_representer(periods.Instant, lambda dumper, data: dumper.represent_scalar(u'tag:yaml.org,2002:str', str(data)))
yaml.add_representer(periods.Period, lambda dumper, data: dumper.represent_scalar(u'tag:yaml.org,2002:str', str(data)))
yaml.add_representer(tuple, lambda dumper, data: dumper.represent_list(data))
yaml.add_representer(unicode, lambda dumper, data: dumper.represent_scalar(u'tag:yaml.org,2002:str', data))


# Functions

def check(yaml_path, name, period_str, test, force, verbose = False):
    scenario = test['scenario']
    # scenario.suggest()
    simulation = scenario.new_simulation(debug = verbose)
    output_variables = test.get(u'output_variables')
    if output_variables is not None:
        output_variables_name_to_ignore = test.get(u'output_variables_name_to_ignore') or set()
        for variable_name, expected_value in output_variables.iteritems():
            if not force and variable_name in output_variables_name_to_ignore:
                continue
            if isinstance(expected_value, dict):
                for requested_period, expected_value_at_period in expected_value.iteritems():
                    assert_near(
                        simulation.calculate(variable_name, requested_period),
                        expected_value_at_period,
                        absolute_error_margin = test.get('absolute_error_margin'),
                        message = u'{}@{}: '.format(variable_name, requested_period),
                        relative_error_margin = test.get('relative_error_margin'),
                        )
            else:
                assert_near(
                    simulation.calculate(variable_name),
                    expected_value,
                    absolute_error_margin = test.get('absolute_error_margin'),
                    message = u'{}@{}: '.format(variable_name, period_str),
                    relative_error_margin = test.get('relative_error_margin'),
                    )


def run_test(force = False, name_filter = None, options_by_path = None):
    if isinstance(name_filter, str):
        name_filter = name_filter.decode('utf-8')
    if options_by_path is None:
        options_by_path = options_by_dir
    for path, options in options_by_path.iteritems():
        if not force and options.get('ignore', False):
            log.info(u'Ignoring {}'.format(path))
            continue
        if not os.path.exists(path):
            log.warning(u'Skipping missing {}'.format(path))
            continue
        if os.path.isdir(path):
            yaml_paths = [
                os.path.join(path, filename)
                for filename in sorted(os.listdir(path))
                if filename.endswith('.yaml')
                ]
        else:
            yaml_paths = [path]

        if options.get('requires'):
            # Check if the required package was successfully imported in tests/base.py
            if getattr(base, options.get('requires')) is None:
                continue

        for yaml_path in yaml_paths:
            filename_core = os.path.splitext(os.path.basename(yaml_path))[0]
            with open(yaml_path) as yaml_file:
                tests = yaml.load(yaml_file)
            tests, error = conv.pipe(
                conv.make_item_to_singleton(),
                conv.uniform_sequence(
                    conv.noop,
                    drop_none_items = True,
                    ),
                )(tests)
            if error is not None:
                embedding_error = conv.embed_error(tests, u'errors', error)
                assert embedding_error is None, embedding_error
                raise ValueError("Error in test {}:\n{}".format(yaml_path, yaml.dump(tests, allow_unicode = True,
                    default_flow_style = False, indent = 2, width = 120)))

            for test in tests:
                test, error = scenarios.make_json_or_python_to_test(
                    tax_benefit_system = tax_benefit_system,
                    default_absolute_error_margin = options.get('default_absolute_error_margin'),
                    default_relative_error_margin = options.get('default_relative_error_margin'),
                    )(test)
                if error is not None:
                    embedding_error = conv.embed_error(test, u'errors', error)
                    assert embedding_error is None, embedding_error
                    raise ValueError("Error in test {}:\n{}\nYaml test content: \n{}\n".format(
                        yaml_path, error, yaml.dump(test, allow_unicode = True,
                        default_flow_style = False, indent = 2, width = 120)))

                if not force and test.get(u'ignore', False):
                    continue
                if name_filter is not None and name_filter not in filename_core \
                        and name_filter not in (test.get('name', u'')) \
                        and name_filter not in (test.get('keywords', [])):
                    continue
                checker = check
                yield checker, yaml_path, test.get('name') or filename_core, unicode(test['scenario'].period), test, \
                    force

def main():
    import argparse
    import logging
    import sys

    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('paths', help = "path (file or directory) of tests to execute", metavar = 'PATH', nargs = '*')
    parser.add_argument('-f', '--force', action = 'store_true', default = False,
        help = 'force testing of tests with "ignore" flag and formulas belonging to "ignore_output_variables" list')
    parser.add_argument('-n', '--name', default = None, help = "partial name of tests to execute")
    parser.add_argument('-v', '--verbose', action = 'store_true', default = False, help = "increase output verbosity")
    args = parser.parse_args()
    logging.basicConfig(level = logging.DEBUG if args.verbose else logging.WARNING, stream = sys.stdout)

    if args.paths:
        options_by_path = collections.OrderedDict()
        for path in args.paths:
            path = os.path.abspath(path).rstrip(os.sep)
            dir = path if os.path.isdir(path) else os.path.dirname(path)
            options = options_by_dir.get(dir)
            if options is None:
                options = dict(
                    calculate_output = False,
                    default_absolute_error_margin = 0.005,
                    )
            options_by_path[path] = options
    else:
        options_by_path = None

    tests_found = False
    for test_index, (checker, yaml_path, name, period_str, test, force) in enumerate(
            run_test(
                force = args.force,
                name_filter = args.name,
                options_by_path = options_by_path,
                ),
            1):
        keywords = test.get('keywords', [])
        title = "Test {}: {} {}{} - {}".format(
            test_index,
            yaml_path,
            u'[{}] '.format(u', '.join(keywords)).encode('utf-8') if keywords else '',
            name.encode('utf-8'),
            period_str,
            )
        print("=" * len(title))
        print(title)
        print("=" * len(title))
        checker(yaml_path, name, period_str, test, force, args.verbose)
        tests_found = True
    if not tests_found:
        print("No test found!")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
