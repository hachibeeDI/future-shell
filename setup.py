#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = open('requirements.txt').read().split('\n')
readme_content = open('README.md').read()


setup(
    name='futures-shell',
    version='0.0.1',
    description='Decorator based toolkit to use JSONRPC easy like Flask',
    long_description=readme_content,
    author='OGURA_Daiki',
    author_email='',
    license='MIT',
    keywords=['future simple'],
    url='https://github.com/hachibeeDI/futures-shell',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only'
    ],
)
