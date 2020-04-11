# -*- coding: utf-8 -*-
# @Time    : 11/4/2020 9:39 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.12 不同集合上元素的迭代.py
# @Software: PyCharm

"""
4.12 不同集合上元素的迭代

chain
"""

from itertools import chain

a = [1, 2, 3, 4]
b = ('x', 'y', 'z')
"""
不要求a和b类型一致，只要是迭代器都可以

比 `for x in a+b:` 高效
"""
for x in chain(a,b):
    print(x)

