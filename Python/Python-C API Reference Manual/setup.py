# -*- coding: utf-8 -*-
# @Time    : 14/6/2020 4:55 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: setup.py
# @Software: PyCharm

# from setuptools import setup, Extension
#
# # my_sample = Extension('sample', sources=["samplemodule.c"])
#
# # my_sample1 = Extension('sampleclass', sources=["sampleclassmodule.c"])
# # my_sample2 = Extension('sampleclass2', sources=["sampleclass2module.c"])
# # setup(ext_modules=[my_sample1, my_sample2])
#
# my_sample_func_fib = Extension('fib', sources=["sample_func_fib.c"]) # `fib` is module name
#
# setup(ext_modules=[my_sample_func_fib])


from setuptools import setup, find_packages, Extension

setup(
    name='fib',
    version='0.1.0',
    packages=find_packages(),
    license='GPL-2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            'fib',
            # the files to compile into our module relative to ``setup.py``
            ['sample_func_fib.c'],
        ),
    ],
)
