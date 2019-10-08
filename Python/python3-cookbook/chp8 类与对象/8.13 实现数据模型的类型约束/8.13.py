# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 10:01 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.13.py
# @Software: PyCharm
"""
8.13 实现数据模型的类型约束

定义某些在属性赋值上面有限制的数据结构, 这种情况下最好使用描述器.
"""

# Descriptor for enforcing types
class Typed:
    expected_type = type(None)

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class Stock:
    price = Float("price")

    def __init__(self, price):
        self.price = price

try:
    stock = Stock(20.5)
    print("Legal input: {}".format(20.5))
except TypeError as e:
    print("Illegal input: ",e)

try:
    stock = Stock("IllegalInput")
    print("Legal input: {}".format("IllegalInput"))
except TypeError as e:
    print("Illegal input: ",e)