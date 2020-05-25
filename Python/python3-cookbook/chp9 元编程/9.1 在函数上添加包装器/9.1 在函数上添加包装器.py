# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:32 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.1 在函数上添加包装器.py
# @Software: PyCharm
"""
9.1 在函数上添加包装器

你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)。
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

def countdown(n):
    """Counts down"""
    while n > 0:
        n -= 1

print("""函数可以作为参数传递进另一个函数：""")
countdown = timethis(countdown)
countdown(100000)

print("""以上方法和下面这样的装饰器定义是等价的：""")
# 等价于 countdown2 = timethis(countdown2)
@timethis
def countdown2(n):
    """Counts down"""
    while n > 0:
        n -= 1

countdown2(100000)