# -*- coding: utf-8 -*-
# @Time    : 7/3/2020 10:38 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.9 排列组合的迭代.py
# @Software: PyCharm

"""
4.9 排列组合的迭代

itertools模块提供了三个函数来解决这类问题:
(1) itertools.permutations(N,r): A(N,r)
(2) itertools.combinations(N,r): C(N,r)
(3) itertools.combinations_with_replacement(): 允许同一个元素被选择多次
"""

from itertools import permutations, combinations, combinations_with_replacement
items = ['a', 'b', 'c']

# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')
for p in permutations(items):
    print(p)

# ('a', 'b')
# ('a', 'c')
# ('b', 'c')
for p in combinations(items,2):
    print(p)

# ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')
for p in combinations_with_replacement(items,3):
    print(p)
