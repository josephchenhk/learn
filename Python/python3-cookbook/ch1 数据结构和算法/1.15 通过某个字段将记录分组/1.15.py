# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 4:36 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.15.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.15 通过某个字段将记录分组

itertools.groupby() 函数对于这样的数据分组操作非常实用
"""

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

"""现在假设你想在按 date 分组后的数据块上进行迭代"""

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first (必须！)
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

"""
一个非常重要的准备步骤是要根据指定的字段将数据排序。 因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将
得不到想要的结果。

当然，由于要先进行排序，这个方法其实运行速度比较慢。如果想提升效率，可以牺牲一点内存，用defaultdict去记录同一个日期 
"""
print("- "*30)
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for date in rows_by_date.keys():
    for r in rows_by_date[date]:
        print(r)