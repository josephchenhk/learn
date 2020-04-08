# -*- coding: utf-8 -*-
# @Time    : 8/4/2020 5:01 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.11 同时迭代多个序列.py
# @Software: PyCharm

"""
4.11 同时迭代多个序列

zip
"""

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
"""
(1, 'w')
(2, 'x')
(3, 'y')
"""
for i in zip(a,b):
    print(i)
    
from itertools import zip_longest
"""
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
"""
for i in zip_longest(a,b):
    print(i)