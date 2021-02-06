# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="github-views-bot",
    version="0.0.2",
    description="bot to increase the number of views on github",
    license="GNU",
    author="Kamil Pawlaczyk",
    author_email="prgmr.kamil.pawlaczyk@gmail.com",
    url="https://github.com/Agil-Dev/github-views-bot",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
