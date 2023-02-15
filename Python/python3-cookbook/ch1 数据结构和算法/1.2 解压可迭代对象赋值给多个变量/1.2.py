# -*- coding: utf-8 -*-
# @Time    : 1/15/2020 3:17 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.2.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.2 解压可迭代对象赋值给多个变量

python里面用星号 * 来匹配不定数目的变量
"""

def recursive_sum(items):
    head, *tail = items
    return head + recursive_sum(tail) if tail else head

items = [1, 10, 7, 4, 5, 9]
print(f"Recursive sum is {recursive_sum(items)}")
