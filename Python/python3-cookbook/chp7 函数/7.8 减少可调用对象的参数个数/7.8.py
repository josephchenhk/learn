# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 12:11 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.8.py
# @Software: PyCharm
"""
7.8 减少可调用对象的参数个数

你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器， 但是它的参数太多了，导致调用时出错。
如果需要减少某个函数的参数个数，你可以使用 functools.partial().
"""

def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial
s1 = partial(spam, 1)    # a = 1
s1(2,3,4)

s2 = partial(spam, d=42) # d = 42
s2(1,2,3)