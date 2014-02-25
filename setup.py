#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Set __version__ in the namespace
execfile('howabout/version.py')

try:
   from setuptools import setup
   kw = {}

except ImportError:
   from distutils.core import setup
   kw = {}

with open('readme.rst', 'rb+') as readme:
   long_description = readme.read()

setup(
   name = 'howabout',
   packages = ['howabout'],
   version = __version__,
   description = 'A library to suggest similar strings.',
   author = 'Charlie Liban',
   author_email = 'charlie@clib.ca',
   maintainer='Charlie Liban',
   maintainer_email='charlie@clib.ca',   

   url = 'https://github.com/clibc/howabout',
   download_url = 'https://github.com/clibc/howabout/zipball/master',
   keywords = ['cli'],
   classifiers = [
      'Programming Language :: Python',
      'License :: OSI Approved :: MIT License',
   ],

   license = 'MIT License',
   long_description = long_description,
   **kw
)     
