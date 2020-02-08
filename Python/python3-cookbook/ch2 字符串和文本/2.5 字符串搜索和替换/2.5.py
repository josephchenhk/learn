# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 5:50 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.5.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.5 字符串搜索和替换

对于简单的替换，用replace即可
"""

text1 = 'yeah, but no, but yeah, but no, but yeah'
print(text1.replace('yeah', 'yep')) # yep, but no, but yep, but no, but yep

"""对于复杂的模式，可以用re.sub"""
import re
text2 = 'Today is 11/27/2012. Tomorrow is 11/28/2012.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2))  # Today is 2012-11-27. Tomorrow is 2012-11-28.

"""如果考虑用相同的模式做多次匹配，可以compile成一个pattern"""
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
print(pattern.sub(r'\3-\1-\2', text2))  # Today is 2012-11-27. Tomorrow is 2012-11-28.

"""对于更复杂的替换，可以自定义函数，即sub接受一个函数作为参数"""
from calendar import month_abbr
def change_date(m):  # m 是一个 re.match 对象
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(pattern.sub(change_date, text2))  # Today is 27 Nov 2012. Tomorrow is 28 Nov 2012.

"""如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替"""
sub_string, n = re.subn(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
print(sub_string) # Today is 2012-11-27. Tomorrow is 2012-11-28.
print(n)          # 2
