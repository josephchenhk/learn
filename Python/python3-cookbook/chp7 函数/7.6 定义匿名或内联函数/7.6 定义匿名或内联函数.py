# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 11:37 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.6 定义匿名或内联函数.py
# @Software: PyCharm
"""
7.6 定义匿名或内联函数

"""

add = lambda x, y: x + y
print(add(2,3))                # 5
print(add("hello ","world"))   # "hello world"

"""
按姓氏排序
"""
names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
res = sorted(names, key=lambda name: name.split()[-1].lower())
print(res)