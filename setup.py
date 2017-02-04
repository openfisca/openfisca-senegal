#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Senegal',
    version='0.4.1',
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
    url='https://github.com/openfisca/senegal',

    data_files=[
        ('share/openfisca/openfisca-senegal',
         ['CHANGELOG.md', 'LICENSE', 'README.md']),
        ],
    extras_require={
        'api': [
            'OpenFisca-Web-Api[paster] == 3.0.1.dev0',
            ],
        'notebook': [
            'notebook',
            'matplotlib',
            ],
        'survey': [
            'OpenFisca-Survey-Manager >= 0.8.2',
            ]
        },
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core == 4.3.3',
        'PyYAML >= 3.10',
        ],
    packages=find_packages(exclude=['openfisca_senegal.tests*']),
    test_suite='nose.collector',
    )
