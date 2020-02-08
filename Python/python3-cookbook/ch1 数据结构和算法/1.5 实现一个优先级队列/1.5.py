# -*- coding: utf-8 -*-
# @Time    : 1/16/2020 2:37 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.5.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.5 实现一个优先级队列

python在做元组的比较时，如果前面的比较已经可以确定结果了，则后面的比较操作就不会发生了
"""

"""
先定义一个不支持排序的实例Item
"""

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Item({self.name})"
    __str__ = __repr__

try:
    print(Item("foo")<Item("bar"))
except TypeError as e:
    print(e)

"""
但是把Item放在元组里面，则可以方便地比较
"""
a = (1, Item("foo"))
b = (2, Item("bar"))
try:
    print(a<b)
except TypeError as e:
    print(e)

"""
据此，我们可以利用heapq模块实现一个简单地优先级队列
"""
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))  # 利用元组从左至右排序的特性
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1] # -1表示取出元组最后一个元素, e.g., (-5, 1, Item(bar)) --> Item(bar)

"""
以下是这个PriorityQueue的使用例子
"""
q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("spam"), 4)
q.push(Item("grok"), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

"""
如果queue的元素已经全部被pop out，则会发生IndexError
"""
try:
    print(q.pop())
except IndexError as e:
    print(f"Error! {e}")