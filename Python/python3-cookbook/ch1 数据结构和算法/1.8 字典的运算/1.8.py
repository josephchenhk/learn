# -*- coding: utf-8 -*-
# @Time    : 1/17/2020 3:35 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.8.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.8 字典的运算

怎样在数据字典中执行一些计算操作（比如求最大值、最小值和排序等）呢？
一个方案是min max sort等函数里面有关键字key，可以利用key=lambda x: x['key']来执行运算
另一个方案是利用zip将key和value反转，然后可以直接按value进行求最大、最小值和排序
"""

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
}

"""
方案一：利用key=lambda x
"""
print(min(prices, key=lambda x: prices[x]))    # >> FB
print(max(prices, key=lambda x: prices[x]))    # >> AAPL
print(sorted(prices, key=lambda x: prices[x])) # >> ['FB', 'HPQ', 'ACME', 'IBM', 'AAPL']

"""
方案二：利用zip对key和value进行反转
"""
print(min(zip(prices.values(), prices.keys())))  # (10.75, 'FB')
print(max(zip(prices.values(), prices.keys())))  # (612.78, 'AAPL')
print(sorted(zip(prices.values(), prices.keys())))  # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

"""
python3-cookbook里面建议用第二种方案
"""