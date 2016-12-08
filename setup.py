#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Senegal',
    version='0.1.0',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        ],
    description=u'Senegalese tax and benefit system for OpenFisca',
    keywords='benefit microsimulation senegal social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-senegal',

    data_files=[
        ('share/openfisca/openfisca-senegal',
         ['CHANGELOG.md', 'LICENSE', 'README.md']),
        ],
    extras_require={
        'test': [
            'nose',
            'PyYAML >= 3.10',
            ],
        'api': [
            'OpenFisca-Web-Api[paster] == 3.0.1.dev0',
            ],
        'notebook': [
            'notebook',
            'matplotlib',
            ]
        },
    install_requires=[
        'OpenFisca-Core >= 4.1.5.dev1, < 5.0',
        ],
    packages=find_packages(exclude=['openfisca_senegal.tests*']),
    test_suite='nose.collector',
    )
