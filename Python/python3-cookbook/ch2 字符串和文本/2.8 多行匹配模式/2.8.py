# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 7:42 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.8.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.8 多行匹配模式

在正则表达式re模块里，点(.)并不能匹配换行符
"""
import re

text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
comment_pattern = re.compile(r'/\*(.*?)\*/')  # 尝试用店(.)去匹配多行文字
print(comment_pattern.findall(text1))  # [' this is a comment ']
print(comment_pattern.findall(text2))  # [] 匹配失败

"""解决方法1：将点( . )改造成同时匹配点和换行符( (?:.|\n) )"""
comment_pattern = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_pattern.findall(text2))  # [' this is a\nmultiline comment ']

"""解决方法2：re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表达式中的点(.)匹配包括换行符在内
的任意字符"""
comment_pattern = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment_pattern.findall(text2))  # [' this is a\nmultiline comment ']