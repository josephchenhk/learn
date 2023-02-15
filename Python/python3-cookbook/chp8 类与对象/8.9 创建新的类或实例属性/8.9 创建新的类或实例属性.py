# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.9 创建新的类或实例属性.py
# @Software: PyCharm
"""
8.9 创建新的类或实例属性

创建一个新的拥有一些额外功能的实例属性类型, 可以通过一个描述器类的形式来定义它的功能.

一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类， 分别为 __get__() 、__set__() 和 __delete__()
这三个特殊的方法。 这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。
"""

# 描述器
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        # 读取属性时，如T.d,返回的是d.get(None, T)的结果，t.d返回的是d.get(t, T)的结果。
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中。例如：
class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
# Calls Point.x.__get__(p,Point)
print(p.x)
# Explanation: x是类变量，所以调用的是Point.x 而不是p.x（实例变量）
# 而Point.x其实是指向-->Integer('x')，这是一个描述器，它的取值由__get__去决定，参数是调用Integer('x')的实例p和类Point
try:
    p.x = 2.3
    print("You successfully set p.x to 2.3")
except TypeError:
    print("You can not set p.x to 2.3")

try:
    p.x = 3
    print("You successfully set p.x to 3")
except TypeError:
    print("You can not set p.x to 3")

"""
同时定义了__get__和__set__方法的描述器称为资料描述器
只定义了__get__的描述器称为非资料描述器
二者的区别是：当属性名和描述器名相同时，在访问这个同名属性时，如果是资料描述器就会先访问描述器，如果是非资料描述器就会先访问属性

Ref: https://zhuanlan.zhihu.com/p/32764345
"""
