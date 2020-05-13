# -*- coding: utf-8 -*-
# @Time    : 7/25/2019 5:02 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.6.py
# @Software: PyCharm
"""
9.6 带可选参数的装饰器

你想写一个装饰器，既可以不传参数给它，比如 @decorator ， 也可以传递可选参数给它，比如 @decorator(x,y,z) 。
"""
from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

"""
可以看到，@logged 装饰器可以同时不带参数或带参数。通过partial方法，达到这个目的了。
"""