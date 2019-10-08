# -*- coding: utf-8 -*-
# @Time    : 9/11/2019 10:48 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 9.10.py
# @Software: PyCharm

"""
9.10 为类和静态方法提供装饰器

给类或静态方法提供装饰器是很简单的，不过要确保装饰器在 @classmethod 或 @staticmethod 之前。
如果你把装饰器的顺序写错了就会出错.
"""
import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()
s.instance_method(10000)
s.class_method(10000)
s.static_method(10000)