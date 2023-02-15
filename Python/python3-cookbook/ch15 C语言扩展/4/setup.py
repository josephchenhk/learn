# -*- coding: utf-8 -*-
# @Time    : 2/6/2020 4:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: setup.py
# @Software: PyCharm

# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      ext_modules=[
        Extension('sample',
                  ['pysample.c'],
                  include_dirs = ['.'],
                  define_macros = [('FOO','1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['.'], # libsample.so在同目录下
                  # libraries = ['sample']
                  )
        ]
)
