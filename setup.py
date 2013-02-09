#!/usr/bin/env python

from setuptools import setup, find_packages

execfile('memories/version.py')

setup(
    name=__package_name__,
    version=__package_version__,
    description=__package_description__,
    author='Will Ballard',
    author_email='wballard@mailfame.net',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'memories = memories.cli:main'
        ]
    },
    install_requires=['lmdb', 'docopt'],
)
