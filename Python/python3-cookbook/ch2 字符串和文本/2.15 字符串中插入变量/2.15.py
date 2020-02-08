# -*- coding: utf-8 -*-
# @Time    : 1/27/2020 7:13 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.15.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.15 字符串中插入变量

"""

"""方法1：使用format"""
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

"""方法2：使用format_map，搭配vars()，但必须实现在变量中定义好："""
name = 'Guido'
n = 37
print(s.format_map(vars()))

"""format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况: """
try:
    print(s.format(name='Guido'))
except KeyError as e:
    print(e)  # KeyError: 'n'

del n # make n undefined in vars()
try:
    print(s.format_map(vars()))
except KeyError as e:
    print(e)  # KeyError: 'n'

"""要处理变量缺失的情况，可以定义一个含有 __missing__() 方法的字典对象："""
class cumstomized_dict(dict):
    def __missing__(self, key):
        return "{" + key + "}"
try:
    print(s.format_map(cumstomized_dict(vars())))  # Guido has {n} messages.
except KeyError as e:
    print(e)

