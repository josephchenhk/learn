# -*- coding: utf-8 -*-
# @Time    : 6/26/2019 9:27 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 12.3.py
# @Software: PyCharm

# 12.3 线程间通信

"""
你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
"""

import heapq
import threading

class Item:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"Item({self._name})"

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]

if __name__=="__main__":
    item1 = Item("ABC")
    item2 = Item("DEF")
    q = PriorityQueue()
    q.put(item1, 1)
    q.put(item2, 3)
    print(q.get())
    print(q.get())
