# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 9:30 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.11.py
# @Software: PyCharm
"""
8.11 简化数据结构的初始化

你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数, 可以在一个基类中写一个公用的 __init__() 函数
"""
import math

# 基类，__init__方法可以被重复利用
class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# 使用基类作初始化（不需要再显式写出__init__）
class Stock(Structure1):
    _fields = ['name', 'shares', 'price']

class Point(Structure1):
    _fields = ['x', 'y']

class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2

"""
>>> s = Stock('ACME', 50, 91.1)
>>> p = Point(2, 3)
>>> c = Circle(4.5)
>>> s2 = Stock('ACME', 50)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "structure.py", line 6, in __init__
        raise TypeError('Expected {} arguments'.format(len(self._fields)))
TypeError: Expected 3 arguments
"""
s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)
try:
    s2 = Stock('ACME', 50)
except TypeError as e:
    print(e)