#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Senegal',
    version='0.8.0',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'Senegalese tax and benefit system for OpenFisca',
    keywords='benefit microsimulation senegal social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/senegal',
    data_files=[
        ('share/openfisca/openfisca-senegal',
         ['CHANGELOG.md', 'LICENSE', 'README.md']),
        ],
    extras_require={
        'notebook': [
            'matplotlib',
            'notebook',
            'OpenFisca-Survey-Manager >= 0.17.5',
            'openpyxl',
            'pandas',
            'scipy',
            'xlrd',
            'xlwt',
            ],
        'survey': [
            'OpenFisca-Survey-Manager >= 0.18.2',
            'scipy',
            ],
        'dev': [
            "autopep8 ==1.4.4",
            "flake8 >=3.5.0,<3.7.0",
            "flake8-print",
            "pycodestyle >=2.3.0,<2.6.0",  # To avoid incompatibility with flake
            "pytest <5.0",
            "openfisca-survey-manager >= 0.18.2",
            "yamllint >=1.11.1,<1.16",
            ]
        },
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 26.0.6, < 27.0',
        ],
    packages=find_packages(exclude=['openfisca_senegal.tests*']),
    )
