#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-actions-example',
    version='1.0',
    description='Project example for building Python project with JFrog products.',
    author='JFrog',
    author_email='matthewam@jfrog.com',
    url='https://github.com/mambroziak/jfrog-python-actions-example',
    packages=['pythonExample'],
    install_requires=['PyYAML>3.11', 'nltk'],
)
