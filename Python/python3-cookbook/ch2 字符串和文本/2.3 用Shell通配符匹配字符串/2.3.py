# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 11:42 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.3.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.3 用Shell通配符匹配字符串

你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串: 用 fnmatch() 和 fnmatchcase()
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))                # True
print(fnmatch('foo.txt', '*.TXT'))                # False
print(fnmatchcase('foo.txt', '*.TXT'))            # True
print(fnmatch('data123.csv', 'data[0-9]*.csv'))   # True