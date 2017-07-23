# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='tftests',
    version='0.1.0',
    description='Playground for working with machine learning',
    long_description=readme,
    author='austinv11',
    author_email='none@email.com',
    url='https://github.com/austinv11/MLExperiments',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)