#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='atmosfera_estandar',
    version='0.0.0',
    author='Enrique Carlos Toomey',
    author_email='enritoomey@gmail.com',
    long_description='This library implemets the International Standard Atmospheric model.',
    packages=find_packages(exclude=["tests"]),
    license="?",
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: Aeronautical Engineering Students',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires=[
        'numpy',# 'pyside' 

    ],
)
