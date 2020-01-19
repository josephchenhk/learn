# -*- coding: utf-8 -*-
# @Time    : 1/19/2020 5:55 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.10.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.10 删除序列相同元素并保持顺序
"""

"""
如果序列上的值都是 hashable 类型（即不可以动态增删），那么可以很简单的利用集合或者生成器来解决这个问题。比如：
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))   # [1, 5, 2, 9, 10]

"""
如果序列上的元素不是 hashable 类型（即可以动态增删，例如list，dict等，tuple则属于可hashable的）, 则set()不能存放，需要加一个
lambda参数进行调整
"""
b = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
try:
    print(list(dedupe(b)))
except TypeError as e:
    print(e)  # unhashable type: 'dict'

def dedupe_non_hashable(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

print(list(dedupe_non_hashable(b, key=lambda x: (x['x'], x['y']))))  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

"""也可以仅仅很对字典里key为x 的元素进行删除（即不管key为y的元素）"""
print(list(dedupe_non_hashable(b, key=lambda x: x['x'])))  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

"""也兼容hashable """
print(list(dedupe_non_hashable(a)))  # [1, 5, 2, 9, 10]
