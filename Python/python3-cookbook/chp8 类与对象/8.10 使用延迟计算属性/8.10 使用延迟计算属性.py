# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.10 使用延迟计算属性.py
# @Software: PyCharm
"""
8.10 使用延迟计算属性

定义一个延迟属性的一种高效方法是通过使用一个描述器类
"""
import math

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

class Circle1:
    def __init__(self, radius):
        self.radius = radius

    # 类作为装饰器时，因为area = lazyproperty(area) = lazyproperty的实例，这个过程会对lazyproperty进行实例化
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

class Circle2:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

# c2 = Circle2(4.0)
# print(c2.area)
# print(c2.area)
# print(c2.perimeter)
# print(c2.perimeter)
# print("-----------------------------\n")

c1 = Circle1(4.0)

"""
c1.area 第一次调用时，因为c1实例中并没有"area"这个attribute（c1.__dict__中只有"radius": {'radius': 4.0}），
但c1里面有装饰器（lazyproperty），将"area"定义成为lazyproperty(area)了，这里lazyproperty作为一个描述器被调用，
所以会调用__get__方法（而不是__call__方法）。
调用了__get__方法后，计算得到面积大小的返回值，并同时通过setattr，在c1.__dict__中添加了"area": {'radius': 4.0, 'area': 50.265}，
之后下一次再调用c1.area的时候，就会通过__getattribute__直接读取__dict__中的数据，而不是重新计算一遍！

python的属性访问和描述符： https://blog.csdn.net/lilong117194/article/details/80111803
"""
print(c1.area)
print(c1.area)

print(c1.perimeter)
print(c1.perimeter)

"""
Python中，如果在创建class的时候写了call()方法， 那么该class实例化出实例后， 实例名()就是调用call()方法。例子：

class Animal(object):
    __call__(self, words):
        print "Hello: ", words

cat = Animal()
cat("I am cat!")

>>> Hello: I am cat!
"""
