# -*- coding: utf-8 -*-
# @Time    : 28/2/2020 5:20 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.4 实现迭代器协议.py
# @Software: PyCharm

"""
4.4 实现迭代器协议

在这段代码中，depth_first() 方法简单直观。 它首先返回自己本身并迭代每一个子节点并 通过调用子节点的 depth_first() 方法(使用 yield from
语句)返回对应元素。
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first() # yiled from 跟一个generator

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

"""
        0
       / \
      1   2
     / \   \
    3   4   5

Node(0)
Node(1)
Node(3)
Node(4)
Node(2)
Node(5)
"""
print("用generator实现node：")
for ch in root.depth_first():
    print(ch)


######################################################
print(" ------------------------------- ")
print("用iterrator实现node：")
class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node) # self._node = Node(0); self._children_iter = iter([Node(1), Node(2)])
            return self._node                      # return Node(0)
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                # next(self) 即会调用 __next__(self) 本身：
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            # 如果self._children_iter是一个空的generator，那么next(self._children_iter)会报StopIteration的错，这个错会被__next__(self)
            # 方法捕获，从而程序正常终止。
            child = next(self._children_iter)      # child = Node(1)
            # 递归调用，child.depth_first() 就会调用 DepthFirstIterator(child) = DepthFirstIterator(Node(1))
            self._child_iter = child.depth_first() # self._child_iter = DepthFirstIterator(Node(1))
            # next(self) 即会调用 __next__(self) 本身：
            # 此时，
            # self._node = Node(0)
            # self._children_iter = iter([Node(1), Node(2)])
            # self._child_iter = DepthFirstIterator(Node(1))
            return next(self)
root = Node2(0)
child1 = Node2(1)
child2 = Node2(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)
