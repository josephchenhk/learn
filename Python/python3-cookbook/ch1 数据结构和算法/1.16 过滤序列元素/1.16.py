# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 5:54 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.16.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.16 过滤序列元素

最简单的过滤序列元素的方法就是使用列表推导。
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])

"""
列表会占用内存，如果想轻量一些，可以用生成器（元组，或者filter）
"""
print((n for n in mylist if n > 0))
print(list((n for n in mylist if n > 0)))  # 元组

print(filter(lambda x: x>0, mylist))
print(list(filter(lambda x: x>0, mylist))) # filter

"""
itertools.compress()可以接受一个mask，将相应位置为True的元素保留
"""
from itertools import compress
mask = [True, False, False, True, True, False, False, True]
print(compress(mylist, mask))
print(list(compress(mylist, mask)))