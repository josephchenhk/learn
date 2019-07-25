# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:54 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 9.4.py
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