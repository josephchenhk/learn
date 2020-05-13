# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:32 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.1.py
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

@timethis
def countdown(n):
    """Counts down"""
    while n > 0:
        n -= 1

countdown(100000)