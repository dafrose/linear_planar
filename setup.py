#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Python install script.

Install with `python setup.py install` or `python setup.py develop` for developer mode."""

from setuptools import setup, find_packages

REQUIREMENTS = ["numpy",
                "nibabel",
                "scipy"]

setup(
    name="linear_planar",
    description="Preprocessing and fitting scripts for double PGSE data",
    version="0.1",
    packages=find_packages(),
    package_data={
        "": ["*.txt", "*.cnf", "*.sh"],
    },
    install_requires=REQUIREMENTS,
    python_requires=">=3.5",
    url="https://github.com/blochchainlab/linear_planar"
)


