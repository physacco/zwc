#!/usr/bin/env python
# encoding: utf-8

import zwc
from setuptools import setup

setup(
  name='zwc',
  version=zwc.__version__,
  description='Chinese word count tool',
  long_description='This is a simple Chinese word count tool that contains a command line program and a Python module.',
  url='https://github.com/physacco/zwc',
  author='physacco',
  author_email='physacco@gmail.com',
  license='MIT',
  py_modules=['zwc'],
  entry_points={ 'console_scripts': [ 'zwc = zwc:main' ] },
  install_requires=['six']
)
