# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 7:34 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.7.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.7 最短匹配模式

本节讨论正则表达式模块 re 的 贪婪模式 vs 非贪婪模式。见例子：
"""
import re

pattern = re.compile(r'"(.*)"')  # . 表示任意字符，* 表示任意个数
text1 = 'Computer says "no."'
print(pattern.findall(text1))  # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
print(pattern.findall(text2))  # ['no." Phone says "yes.']

"""在这个例子中，模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。 但是在正则表达式中*操作符是贪婪的，因此匹配操作会查找最长的
可能匹配.
为了修正这个问题，可以在模式中的*操作符后面加上?修饰符: 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短
的可能匹配.
"""
pattern_non_greedy = re.compile(r'"(.*?)"')
print(pattern_non_greedy.findall(text2))  # ['no.', 'yes.']  This is what we want!