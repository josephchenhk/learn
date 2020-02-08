# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 7:20 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.6.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.6 字符串忽略大小写的搜索替换

为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供 re.IGNORECASE 标志参数:
"""

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))      # ['PYTHON', 'python', 'Python']
print(re.sub('python', 'snake', text, flags=re.IGNORECASE)) # UPPER snake, lower snake, Mixed snake

"""但这里把所有匹配都替换成小写的snake了，能不能按照规则分别换成全大写、全小写和首字母大写呢？
答案是需要自定义一个函数
"""
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
# 这里matchcase('snake')就是一个函数，相当于25行的replace，而传入的参数则为re.sub搜索匹配的match对象（即m）
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)) # UPPER SNAKE, lower snake, Mixed Snake