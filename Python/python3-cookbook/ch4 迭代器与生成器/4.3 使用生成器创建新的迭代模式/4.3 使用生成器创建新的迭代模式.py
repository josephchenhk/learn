# -*- coding: utf-8 -*-
# @Time    : 28/2/2020 3:38 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.3 使用生成器创建新的迭代模式.py
# @Software: PyCharm

"""
4.3 使用生成器创建新的迭代模式

"""


def frange(start, end, increment):
    x = start
    while x<end:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print("---------------------------\n")
f = frange(0, 4, 0.5)
print(next(f), next(f), next(f))
