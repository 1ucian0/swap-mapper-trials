# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="swap-mapper-trials",
    description="More trials are better results(?)",
    author="gines-carrascal",
    author_email="gines-carrascal@qiskit.org",
    packages=find_packages(exclude=['test*']),
    install_requires=["qiskit-terra"]
)
