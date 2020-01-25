# -*- coding: utf-8 -*-
# @Time    : 1/25/2020 11:46 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.11.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.11 删除字符串中不需要的字符

strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作。 默认情况下，这些方法会去除空白字符，
但是你也可以指定其他字符。比如：
"""

s = ' hello world \n'
# 两边删空格
print(s.strip())  # "hello world"
# 左边删空格
print(s.lstrip()) # "hello world \n"
# 右边删空格
print(s.rstrip()) # " hello world"


# Character stripping
t = '-----hello====='
# 从左边删除所有"-"
print(t.lstrip('-')) # "hello====="
# 从右边删除所有"="
print(t.strip('=')) # "-----hello"
# 从左右两边删除所有"-="
print(t.strip('-=')) # "hello"

"""strip()结合生成器使用，非常有效：
表达式 lines = (line.strip() for line in f) 执行数据转换操作。 这种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列
表中去。 它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。
"""

f = ["Hello,  ", "How are you?  ", "     My name is Joseph.   "]
lines = (line.strip() for line in f)
print(lines) # <generator object <genexpr> at 0x0000027C1B6F9AC8>
for line in lines:
    print(line)

"""
>>>Hello,
>>>How are you?
>>>My name is Joseph.
"""