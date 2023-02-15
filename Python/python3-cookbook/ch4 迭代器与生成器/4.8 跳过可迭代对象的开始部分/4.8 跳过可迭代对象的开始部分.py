# -*- coding: utf-8 -*-
# @Time    : 4/3/2020 7:01 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.8 跳过可迭代对象的开始部分.py
# @Software: PyCharm

"""
4.8 跳过可迭代对象的开始部分

itertools.dropwhile(): 丢弃
itertools.islice():   切片
"""

data = ["#Drop me",
        "#Drop me again",
        "Don't drop me",
        "Please! Don't drop me"
        ]

from itertools import dropwhile, islice

print("Use dropwhile:")
# 从第一个元素开始数，一直丢弃直到predicate的条件不再符合为止
for d in dropwhile(lambda x: x.startswith("#"), data):
    print(d)

print("\nUse islice:")
# 也可以通过切片的方式达到同样的效果(这里相当于切片 [2:] )
for d in islice(data, 2, None):
    print(d)

##########################################################
from io import StringIO

many_lines = \
"""# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
"""
# print(many_lines)
s = StringIO(many_lines)

print(list(s.readlines()))


# ???奇怪
for line in dropwhile(lambda x: x.startswith("#"), s.readlines()):
    print(line, end='')

s.close()
