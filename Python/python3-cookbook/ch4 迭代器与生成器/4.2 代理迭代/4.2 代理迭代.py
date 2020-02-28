# -*- coding: utf-8 -*-
# @Time    : 28/2/2020 3:38 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.2 代理迭代.py
# @Software: PyCharm

"""
4.2 代理迭代

Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象。
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__=="__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)