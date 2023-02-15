# -*- coding: utf-8 -*-
# @Time    : 5/1/2022 11:27 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

import module
from module import A

# for classes imported into your module:
A = type('A', (A,), {'__slots__': ('foo',)})
# for classes which will be instantiated by the `module` itself:
module.B = type('B', (module.B,), {'__slots__': ('bar',)})

a = A()
a.x = 1
a.foo = 2

b = a.b
b.z = 3
b.bar = 4
