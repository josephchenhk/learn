# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 5:41 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.23.py
# @Software: PyCharm
"""
8.23 循环引用数据结构的内存管理

import weakref

import gc
>>> gc.collect() # force collection
"""

class Data:
    def __del__(self):
        print('Data.__del__')

# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self._parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)   # 父节点引用子节点
        child._parent = self           # 反过来，子节点也引用父节点

a = Data()
del a      # immediately delete
b = Node()
del b      # immediately delete
c = Node()
c.add_child(Node())  # c加了一个子节点之后，情况变得复杂了
del c      # not deleted (no message)
print("""可以看到，最后一个的删除时打印语句没有出现。原因是Python的垃圾回收机制是基于简单的引用计数。 当一个对象的引用
数变成0的时候才会立即删除掉。而对于循环引用这个条件永远不会成立。 因此，在上面例子中最后部分，父节点和孩子节点互相拥有
对方的引用，导致每个对象的引用计数都不可能变成0。""")


import weakref

class Node2(Node):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)


print("---------------------start--------------------\n")
d = Node2()
d.add_child(Node2())  # d加了一个子节点之后，但由于是弱引用，不会影响删除 [oh no! not correct??]
del d                 # immediately delete [No message?? why???]
print("----------------------end---------------------\n")