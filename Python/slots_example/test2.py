# -*- coding: utf-8 -*-
# @Time    : 5/1/2022 11:37 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test2.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the 
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

import module

module.A = type('A', (module.A,), {'__slots__': ('foo',)})
module.B = type('B', (module.B,), {'__slots__': ('bar',)})

# note that we import `module_3rd_party` AFTER we patch the `module`
from module_3rd_party import get_instance

a = get_instance()
a.x = 1
a.foo = 2

b = a.b
b.z = 3
b.bar = 4
