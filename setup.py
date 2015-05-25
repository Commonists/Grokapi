#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Setup script."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import grokapi
    version = grokapi.__version__
except ImportError:
    version = 'Undefined'

with open('requirements.txt') as requirements_file:
    requirements = list(requirements_file.readlines())


classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities'
]
packages = ['grokapi']

setup(
    name='MediaCollectionDB',
    version=version,
    author='Commonists',
    author_email='ps.huard@gmail.com',
    url='http://github.com/Commonists/Grokapi',
    description='Media Collection database for MediaWiki',
    long_description=open('README.md').read(),
    license='MIT',
    packages=packages,
    install_requires=requirements,
    classifiers=classifiers
)