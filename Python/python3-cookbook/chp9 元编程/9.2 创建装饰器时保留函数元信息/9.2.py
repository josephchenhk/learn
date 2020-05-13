# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:35 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.2.py
# @Software: PyCharm
"""
9.2 创建装饰器时保留函数元信息

你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。
任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数。
"""
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    """Counts down"""
    while n > 0:
        n -= 1

countdown(100000)
print(countdown.__doc__)          # Counts down
print(countdown.__annotations__)  # {'n': <class 'int'>}