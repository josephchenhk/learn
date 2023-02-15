# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:54 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.4 定义一个带参数的装饰器.py
# @Software: PyCharm
"""
9.4 定义一个带参数的装饰器

三重def
"""

from functools import wraps
import logging

def logged(level, name=None, message=None):   # 第一重，接收参数
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):   # 第二重，接收原函数
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):  # 第三重，实现修改功能
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

logging.basicConfig(level=logging.DEBUG)
print(add(2,3))
spam()

"""
定义一个接受参数的包装器看上去比较复杂主要是因为底层的调用序列。特别的，如果你有下面这个代码：

@decorator(x, y, z)
def func(a, b):
    pass
装饰器处理过程跟下面的调用是等效的;

def func(a, b):
    pass
func = decorator(x, y, z)(func)
decorator(x, y, z) 的返回结果必须是一个可调用对象，它接受一个函数作为参数并包装它， 可以参考9.7小节中另外一个可接受参数的包装器例子。
"""
