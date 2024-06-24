#! /usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='OpenFisca-Senegal',
    version='0.11.1',
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
            'OpenFisca-Survey-Manager >= 2, <=2.3',
            'openpyxl',
            'pandas',
            'scipy',
            'xlrd',
            'xlwt',
            ],
        'survey': [
            'OpenFisca-Survey-Manager >= 2, <=2.3',
            'scipy',
            ],
        'dev': [
            "autopep8 ==1.5.5",
            "flake8 >=6.0.0,<7.0.0",
            "flake8-print",
            "openfisca-survey-manager >= 2, <=2.3",
            "pytest >= 7.2.2, < 8.0.0",
            "yamllint >=1.11.1,<1.27",
            "pandas",
            ],
        'ceq': [
            "openfisca-ceq >= 0.4.1",
            ],
        },
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 41, < 42.0',
        ],
    packages=find_packages(exclude=['openfisca_senegal.tests*']),
    )
