#!/usr/bin/env python
# encoding: utf-8

import sys
from setuptools import setup

if sys.platform == 'win32':
    scripts = ['zwc.bat']
else:
    scripts = ['zwc']

setup(
  name='zwc',
  version='0.2.0',
  description='Chinese word count tool',
  long_description='This is a simple Chinese word count tool that contains a command line program and a Python module.',
  url='https://github.com/physacco/zwc',
  author='physacco',
  author_email='physacco@gmail.com',
  license='MIT',
  py_modules=['zwc', 'zwc_cli'],
  scripts=scripts,
  install_requires=['six']
)
