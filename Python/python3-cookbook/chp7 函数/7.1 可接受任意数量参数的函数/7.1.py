# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 7:15 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.1.py
# @Software: PyCharm
"""
7.1 可接受任意数量参数的函数


为了能让一个函数接受任意数量的位置参数，可以使用一个*参数;  [*args]
为了接受任意数量的关键字参数，使用一个以**开头的参数.       [**kwargs]

值得注意的是：一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数。 有一点要注意的是，
在*参数后面仍然可以定义其他参数。
"""

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass