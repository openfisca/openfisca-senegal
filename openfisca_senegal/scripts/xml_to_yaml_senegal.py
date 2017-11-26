# -*- coding: utf-8 -*-

''' xml_to_yaml_senegal.py : Parse XML parameter files for Openfisca-senegal and convert them to YAML files. Comments are NOT transformed.

Usage :
  `python xml_to_yaml_senegal.py output_dir`
or just (output is written in a directory called `yaml_parameters`):
  `python xml_to_yaml_senegal.py`
'''

import sys
import os

from openfisca_senegal.senegal_taxbenefitsystem import COUNTRY_DIR
from openfisca_core.scripts.migrations.v16_2_to_v17 import xml_to_yaml


if len(sys.argv) > 1:
    target_path = sys.argv[1]
else:
    target_path = os.path.join(COUNTRY_DIR, 'parameters')

legislation_xml_info_list = [(os.path.join(COUNTRY_DIR, 'parameters.xml'), [])]

xml_to_yaml.write_parameters(legislation_xml_info_list, target_path)
