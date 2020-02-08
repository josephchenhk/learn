# -*- coding: utf-8 -*-
# @Time    : 1/25/2020 11:33 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.10.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.10 在正则式中使用Unicode

默认情况下 re 模块已经对一些Unicode字符类有了基本的支持。 比如， \\d 已经匹配任意的unicode数字字符了：
"""

import re

num = re.compile('\d+')

# ASCII digits
print(num.match('123'))                 # <re.Match object; span=(0, 3), match='123'>

# Arabic digits
print(num.match('\u0661\u0662\u0663'))  # <re.Match object; span=(0, 3), match='١٢٣'>

"""实在太复杂了！！"""