#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='django-adminlte2',
    version=open('VERSION').read().strip(),
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/adamcharnock/django-adminlte2',
    license='MIT',
    description='Admin LTE templates, admin theme, and template tags for Django',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    include_package_data=True,
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        'django',
    ],
)
