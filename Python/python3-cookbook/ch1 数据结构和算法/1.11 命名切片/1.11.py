# -*- coding: utf-8 -*-
# @Time    : 1/21/2020 11:01 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.11.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.11 命名切片

如果你的程序包含了大量 *不忍直视* 的硬编码切片，并且你想清理一下代码，可以用slice去命名切片：
"""

record = '....................100 .......513.25 ..........'

"""Urgly way: """
cost = int(record[20:23]) * float(record[31:37])
print(f"Urgly cost: {cost}")

"""Elegant way: """
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(f"Elegant cost: {cost}")

"""
如果你有一个切片对象a，你可以分别调用a.start, a.stop, a.step属性来获取起始位置、终止位置和步长信息：
"""
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

"""
并且可以通过indices(size)方法将这个切片对象映射到一个已知大小的序列上，返回一个三元组(start, stop, step)
"""
s = "HelloWorLd!!"
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
