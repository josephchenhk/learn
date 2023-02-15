# -*- coding: utf-8 -*-
# @Time    : 1/21/2020 5:15 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.12.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.12 序列中出现次数最多的元素

collections.Counter 类就是专门为这类问题而设计的. 作为输入， Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)

# word_counts本身是一个字典形式
print(word_counts)  # Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

# 但word_counts同时是一个object，包含更丰富的信息，包括可以提取最高频的N的元素，以及作集合运算等
print(word_counts.most_common(3))  # [('eyes', 8), ('the', 5), ('look', 4)]

morewords = ['why','are','you','not','looking','in','my','eyes']
a = Counter(words)
b = Counter(morewords)
print(a + b)
print(a - b)

"""
毫无疑问， Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 在解决这类问题的时候你应该优先选择它，
而不是手动的利用字典去实现。
"""
