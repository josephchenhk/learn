# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 6:29 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.18.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.18 映射名称到序列元素

collections.namedtuple可以认为是一个tuple，但是里面的元素带有名字
"""

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr, sub.joined)

"""
使用namedtuple可以领到语义更清晰
"""
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

records = [["AAPL", 100, 301.5], ["IBM", 200, 144.2]]
print(compute_cost(records))  # 100 * 301.5 + 200 * 144.2 = 58990.0

stock1 = Stock("AAPL", 100, 301.5)
stock2 = Stock("IBM", 200, 144.2)
records = [stock1, stock2]
print(compute_cost(records))  # 100 * 301.5 + 200 * 144.2 = 58990.0

"""
需要注意namedtuple不可随意修改值，否则会报错
"""
try:
    stock1.shares = 150
except AttributeError as e:
    print(e)  # AttributeError: can't set attribute

"""
不过，如果你真的需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法， 它会创建一个全新的命名元组并将对应的字段用新的
值取代。比如：
"""
stock1 = stock1._replace(shares=150)
print(stock1)

"""
这个方法还适用于批量修改，可以用一个字典去修改namedtuple
"""
data = {"name": "Modified-AAPL", "shares": 101, "price": 302.5}
stock1 = stock1._replace(**data)
print(stock1)