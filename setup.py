#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

kw = {}

# Set __version__ in the namespace
with open('howabout/version.py') as file:
   exec(file.read())

with open('readme.rst', 'rb+') as readme:
   long_description = readme.read().decode('utf-8')

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
   install_requires = [
      'six == 1.8.0',
   ],
   license = 'MIT License',
   long_description = long_description,
   **kw
)     
