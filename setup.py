#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join, dirname

from setuptools import setup, find_packages

kw = {}
version = '1.2.0'

with open(join(dirname(__file__), 'readme.rst'), 'rb+') as file:
    long_description = file.read().decode('utf-8')

setup(
    name='howabout',
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,

    version=version,
    description='A library to suggest similar strings.',
    author='Charlie Liban',
    author_email='charlie@clib.ca',
    maintainer='Charlie Liban',
    maintainer_email='charlie@clib.ca',

    url='https://github.com/clibc/howabout',
    download_url='https://github.com/clibc/howabout/zipball/master',
    keywords=['cli'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'six == 1.8.0',
    ],
    license='MIT License',
    long_description=long_description,
    **kw
)     
