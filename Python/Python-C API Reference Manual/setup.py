# -*- coding: utf-8 -*-
# @Time    : 14/6/2020 4:55 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: setup.py
# @Software: PyCharm

from setuptools import setup, Extension

my_sample = Extension('sample', sources=["samplemodule.c"])
setup(ext_modules=[my_sample])