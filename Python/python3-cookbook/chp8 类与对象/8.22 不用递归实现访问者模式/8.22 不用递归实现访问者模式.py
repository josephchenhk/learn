# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 3:57 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.22 不用递归实现访问者模式.py
# @Software: PyCharm
"""
8.22 不用递归实现访问者模式

递归超过嵌套层级限制而失败时，可以考虑用生成器（yield）去处理。
"""
import types

# 所有的·被操作对象·都是Node
class Node:
    pass

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

# 是一个Node
class Add(BinaryOperator):
    pass

# 是一个Node
class Sub(BinaryOperator):
    pass

# 也是一个Node
class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()

        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__   # visit_Add, visit_Sub, visit_Number ...
        meth = getattr(self, methname, None) # self.__class__=__main__.Evaluator, 这里的self其实是Evaluator的实例，而不仅仅是NodeVisitor的实例
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

# 真正做数值计算时，才调用的类
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)


t1 = Sub(Number(3), Number(4))
t2 = Add(t1, Number(1))

# Evaluate it
e = Evaluator()
print(e.visit(t1))  # Outputs -1
print(e.visit(t2))  # Outputs 0