#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'HardUpHumble',
    version = '0.1',
    description = 'HardUpHumble is a program that allows you to monitor the cost of games.',
    author = 'Matt Copperwaite',
    author_email = 'matt@copperwaite.net',
    url = 'https://github.com/yamatt/huh/',
    packages=["huh"],
    install_requires = [
        "pyyaml",
        "requests"
    ],
    scripts=['huh/huh_get_price', 'huh/huh'],
    license = "AGPLv3",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ]
)
