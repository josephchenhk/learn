# -*- coding: utf-8 -*-
# @Time    : 1/18/2020 12:32 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.9.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.9 查找两字典的相同点

为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作。比如：
"""

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common
print(a.keys() & b.keys())    # { 'x', 'y' }

# Find keys in a that are not in b
print(a.keys() - b.keys())    # { 'z' }

# Find (key,value) pairs in common
print(a.items() & b.items())  # { ('y', 2) }