#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ctelib',
    version='0.1',
    author='Raphael Valyi',
    author_email='raphael.valyi@akretion.com',
    url='https://github.com/akretion/ctelib',
    description='ctelib: Conhecimento de Transporte Eletrônico library for Brazil',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    keywords='CT-e ERP Odoo',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    zip_safe=False,
)
