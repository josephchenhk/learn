# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 7:34 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.1.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.1 使用多个界定符分割字符串

string 对象的 split() 方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格。 当你需要更加
灵活的切割字符串的时候，最好使用 re.split() 方法：
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line)) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

"""
当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。 如果使用了捕获分组，那么被匹配的文本也将
出现在结果列表中。
"""
print(re.split(r'(;|,|\s)\s*', line)) # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

"""
如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的话， 确保你的分组是非捕获分组，形如 (?:...) 。
"""
print(re.split(r'(?:,|;|\s)\s*', line)) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
