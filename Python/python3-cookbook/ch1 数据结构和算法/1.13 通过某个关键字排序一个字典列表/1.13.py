# -*- coding: utf-8 -*-
# @Time    : 1/21/2020 5:24 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.13.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.13 通过某个关键字排序一个字典列表

你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表. 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样
的数据结构。
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

"""
itemgetter() 函数也支持多个 keys，比如下面的代码
"""
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

"""
itemgetter() 有时候也可以用 lambda 表达式代替，比如：
"""
rows_by_fname2 = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname2 = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_fname==rows_by_fname2)
print(rows_by_lfname==rows_by_lfname2)

"""
这种方案也不错。但是，使用 itemgetter() 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 itemgetter() 方式。
此外，除了sorted()之外，max()和min()函数也提供key参数进行指定
"""
