#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Senegal',
    version='0.10.1',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description='Senegalese tax and benefit system for OpenFisca',
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
            'OpenFisca-Survey-Manager >= 0.38.1, <=1.0',
            'openpyxl',
            'pandas',
            'scipy',
            'xlrd',
            'xlwt',
            ],
        'survey': [
            'OpenFisca-Survey-Manager >= 0.38.1, <=1.0',
            'scipy',
            ],
        'dev': [
            "autopep8 ==1.4.4",
            "openfisca-ceq >= 0.3",
            "flake8 >=3.5.0,<3.7.0",
            "flake8-print",
            "openfisca-survey-manager >= 0.38.1, <=1.0",
            "pycodestyle >=2.3.0,<2.6.0",  # To avoid incompatibility with flake
            "pytest <6.0",
            "yamllint >=1.11.1,<1.21",
            ],
        'ceq': [
            "openfisca-ceq >= 0.3",
            ],
        },
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 34.6.7, < 35.0',
        ],
    packages=find_packages(exclude=['openfisca_senegal.tests*']),
    )
