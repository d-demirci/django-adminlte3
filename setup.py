#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='django-adminlte-3',
    version=open('VERSION').read().strip(),
    author='d3n1z',
    author_email='d3n1z@protonmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/d-demirci/django-adminlte3',
    license='MIT',
    description='Admin LTE templates, admin theme, and template tags for Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        'django',
    ],
    python_requires='>=3.6',
)
