# -*- coding: utf-8 -*-
# @Time    : 1/16/2020 2:14 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.4.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.4 查找最大或最小的N个元素

heapq模块有两个函数：nlargest()和nsmallest() 可以完美解决这个问题
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(f"3 largest: {heapq.nlargest(3, nums)}")
print(f"3 smallest: {heapq.nsmallest(3, nums)}")

"""
对于等更复杂的数据结构，heapq支持key参数进行指定对比对象
"""
portfolio = [
    {'name': 'IBM', 'share': 100, 'price': 91.1},
    {'name': 'AAPL', 'share': 50, 'price': 543.22},
    {'name': 'FB', 'share': 200, 'price': 21.09},
    {'name': 'HPQ', 'share': 35, 'price': 31.75},
    {'name': 'YHOO', 'share': 45, 'price': 16.35},
    {'name': 'ACME', 'share': 75, 'price': 115.65},
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(f"3 cheapest: {cheap}")
volume = heapq.nlargest(3, portfolio, key=lambda s: s['share'])
print(f"3 largest volume: {volume}")

"""
可以将普通的列表heapify，这样对数据结构的最小值永远在第一个，即heap[0]；当调用heapq.heappop()之后，会将heap[0] pop out出来，
而在第一个位置替换成省下元素里的最小值
"""
heap = list(nums)
heapq.heapify(heap)
print(f"heap: {heap}")
print(f"pop out first element: {heapq.heappop(heap)}") # 注意：和 heap.pop()命令不同！
print(f"heap: {heap}")