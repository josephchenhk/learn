# -*- coding: utf-8 -*-
# @Time    : 8/9/2019 5:05 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.9.py
# @Software: PyCharm
"""
9.9 将装饰器定义为类

为了将装饰器定义成一个实例，你需要确保它实现了 __call__() 和 __get__() 方法
"""

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class T(object):
    name = 'name'
    def hello(self):
        print('hello')
t = T()

print()