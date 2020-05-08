# -*- coding: utf-8 -*-
# @Time    : 7/5/2020 7:19 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.15 顺序迭代合并后的排序迭代对象.py
# @Software: PyCharm

"""
4.15 顺序迭代合并后的排序迭代对象

问题
你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
"""

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# 1
# 2
# 4
# 5
# 6
# 7
# 10
# 11
for c in heapq.merge(a, b):
    print(c)

"""
有一点要强调的是 heapq.merge() 需要所有输入序列必须是排过序的。 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检
测。 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。
"""