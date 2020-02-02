# -*- coding: utf-8 -*-
# @Time    : 1/29/2020 4:57 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.18.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.18 字符串令牌解析

你有一个字符串，想从左至右将其解析为一个令牌流(即将每一部分对应到相应的变量)。例如你希望做如下匹配：
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
"""
text = 'foo = 23 + 42 * 10'

# 需要用到正则表达式（?P<TOKENNAME> 用于给一个模式命名，供后面使用）
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

"""调用scanner可以不断调用match去匹配文本："""
scanner = pattern.scanner(text)
while True:
    matched_text = scanner.match()
    if matched_text is not None:
        # matched_text.lastgroup给出名字（即?P<TOKENNAME>所定义），matched_text.group()给出匹配的字符串
        print(matched_text, ":   ", matched_text.group(), matched_text.lastgroup)
    else:
        break

"""也可以做成一个生成器："""
def token_generator():
    for m in iter(scanner.match, None):
            yield (m.lastgroup, m.group())
print("--------- 生成器 ---------")
scanner = pattern.scanner(text)
for t in token_generator():
    print(t)
