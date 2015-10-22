#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='orgflow',
    version='0.0',

    description='Orgflow Task Tracker',
    long_description=long_description,

    url='https://github.com/tomislacker/orgflow',

    author='Ben Tomasik',
    author_email='b.tomasik+orgflow@gmail.com',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='task track organization',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        'alembic',
        'docopt',
        'netaddr',
        'pyaml',
    ],

    extras_require={
        'dev': ['nose', 'pep8'],
        'test': ['coverage'],
    },

    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
        ],
    },
)
