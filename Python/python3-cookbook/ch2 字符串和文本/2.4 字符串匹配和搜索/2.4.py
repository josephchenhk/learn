# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 11:52 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.4.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.4 字符串匹配和搜索

这一节基本上就是正则表达式匹配 re 模块的使用
"""
import re

text1 = '11/27/2012'
print(re.match(r'\d+/\d+/\d+', text1))  # <re.Match object; span=(0, 10), match='11/27/2012'>:  用r'...'表示 raw string，否则需要写成 '\\d+/\\d+/\\d+'
print(re.match(r'\d+/\d+/\d+', text1).group())  # 提取数据(确定有match才可以group，否则返回None不能调用group()

"""match是从字符串开始位置去匹配，如果想从任意位置去匹配，需要用findall"""
text2= 'some_text 11/27/2012'
print(re.match(r'\d+/\d+/\d+', text2))   # None
print(re.findall(r'\d+/\d+/\d+', text2)) # ['11/27/2012']

"""如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象"""
pattern = re.compile(r'\d+/\d+/\d+')
print(pattern.match(text2))   # None
print(pattern.findall(text2)) # ['11/27/2012']

"""在定义正则式的时候，通常会利用括号去捕获分组"""
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
print(pattern.match(text1).group(0))  # 11/27/2012
print(pattern.match(text1).group(1))  # 11
print(pattern.match(text1).group(2))  # 27
print(pattern.match(text1).group(3))  # 2012
print(pattern.match(text1).groups())  # ('11', '27', '2012')

"""findall返回列表list， finditer返回生成器"""
text3 = '11/27/2012 12/8/2013'
print(pattern.findall(text3))  # [('11', '27', '2012'), ('12', '8', '2013')]
print(pattern.finditer(text3)) # <callable_iterator object at 0x000001BF8CAE3D88>
print(list(pattern.finditer(text3))) # [<re.Match object; span=(0, 10), match='11/27/2012'>, <re.Match object; span=(11, 20), match='12/8/2013'>]

"""如果你想精确匹配，确保你的正则表达式以$结尾"""
text4 = '11/27/2012abcdef'
pattern = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(pattern.match(text4))  # None
print(pattern.match(text1))  # <re.Match object; span=(0, 10), match='11/27/2012'>
