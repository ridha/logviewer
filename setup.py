#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


requirements = [
    "aiohttp",
    "aiohttp_jinja2"
]

setup(
    name='logviewer',
    version='1.0.4',
    description='Log monitoring in your browser',
    author='Abdul Kader Maliyakkal',
    author_email='akm.mail@gmail.com',
    url='https://github.com/ridha/logviewer',
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'logviewer = logviewer.server:main'
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
