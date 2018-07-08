#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='packagify',
    version='0.1.0',
    description='python scripts to package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmsv/python-packagify',
    author='James Vickery',
    author_email='dev@jamesvickery.net',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.3, <4',
    keywords='python package generator setup setuptools',
    packages=['packagify'],
    entry_points={
        'console_scripts': [
            'packagify=packagify:cli',
        ],
    },
    project_urls={
        'Source': 'https://github.com/jmsv/python-packagify',
        'Bug Reports': 'https://github.com/jmsv/python-packagify/issues',
    },
)

