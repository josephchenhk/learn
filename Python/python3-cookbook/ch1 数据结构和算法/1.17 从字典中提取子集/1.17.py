# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 6:14 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.17.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.17 从字典中提取子集

最简单的方式是使用字典推导:
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1) # {'AAPL': 612.78, 'IBM': 205.55}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2) # {'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}

# 虽然dict也可以做到字典{}能做到的，但效率较慢
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3) # {'AAPL': 612.78, 'IBM': 205.55}
