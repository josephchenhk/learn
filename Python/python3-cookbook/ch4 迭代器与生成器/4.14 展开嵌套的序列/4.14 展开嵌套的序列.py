# -*- coding: utf-8 -*-
# @Time    : 7/5/2020 7:14 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.14 展开嵌套的序列.py
# @Software: PyCharm

"""
4.14 展开嵌套的序列

可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题
"""

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types): # type(x) not in ignore_types:
            yield from flatten(x)
            # yield from flatten(x) 在这里等价于：
            #
            # for i in flatten(x):
            #     yield i
        else:
            yield x

items = [1, 2, ["helo", 4, [5, 6], 7], 8]

# Produces [1, 2, 'helo', 4, 5, 6, 7, 8]
print(list(flatten(items)))
