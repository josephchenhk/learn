# -*- coding: utf-8 -*-
# @Time    : 7/25/2019 6:42 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.8.py
# @Software: PyCharm
"""
9.8 将装饰器定义为类的一部分

你想在类中定义装饰器，并将其作用在其他函数或方法上.
"""
from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

# As an instance method
a = A()
@a.decorator1
def spam():
    pass
# As a class method
@A.decorator2
def grok():
    pass

spam()
grok()
