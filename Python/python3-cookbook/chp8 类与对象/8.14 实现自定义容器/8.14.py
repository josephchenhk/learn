# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 10:29 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.14.py
# @Software: PyCharm
"""
8.14 实现自定义容器

你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典.

collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。 比如你想让你的类支持迭代，那就让你的类继承
collections.Iterable (同时还要实现__iter__() 方法，否则实例化的时候会出错)
"""
import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "[" + ",".join((str(i) for i in self._items)) + "]"

    __repr__ = __str__

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

items = SortedItems([5, 1, 3])
print(items)  # [1,3,5]
items.add(2)
print(items)  # [1,2,3,5]


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

    def __str__(self):
        return "[" + ",".join((str(i) for i in self._items)) + "]"

    __repr__ = __str__

a = Items([1, 2, 3])
print(a)    # [1, 2, 3]
a.append(4) # append 操作其实是先调用__len__，得到列表长度；然后调用insert，将值插到
print(a)    # [1, 2, 3, 4]
a.count(2)
a.remove(3)
print(a)    # [1, 2, 4]
