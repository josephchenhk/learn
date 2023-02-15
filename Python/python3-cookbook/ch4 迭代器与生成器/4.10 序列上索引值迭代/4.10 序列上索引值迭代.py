# -*- coding: utf-8 -*-
# @Time    : 8/4/2020 11:08 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.10 序列上索引值迭代.py
# @Software: PyCharm

"""
4.10 序列上索引值迭代

你想在迭代一个序列的同时跟踪正在被处理的元素索引: 内置的 enumerate() 函数可以很好的解决这个问题
"""

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1): # start counting from 1
    print(idx, val)
