# -*- coding: utf-8 -*-
# @Time    : 7/25/2019 3:42 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.5.py
# @Software: PyCharm
"""
9.5 可自定义属性的装饰器

你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为。
"""
from functools import wraps, partial
import logging
# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        # @attach_wrapper(wrapper)   # 加了这个装饰器，才可以使用 add.set_message('Add called')
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

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
add(2, 3)
print("-------------------修改了message-------------------\n")
add.set_message('Add called')
add(2,3)

"""
流程解释：

add(2,3) = logged(logging.DEBUG)(add)(2,3) = decorate(add)(2,3) = wrapper(2,3)
         --> log.log(level, logmsg) --> func(*args, **kwargs), 这里func是add，即add(2,3) --> 5

add.set_message('Add called') = logged(logging.DEBUG)(add).set_message('Add called')
         --> decorate(add).set_message('Add called') --> 又遇到装饰器 @attach_wrapper(wrapper)
         --> attach_wrapper(wrapper)(set_message)('Add called')，进入attach_wrapper函数，obj=wrapper, func=None
         --> 所以return partial(attach_wrapper, obj)=attach_wrapper(func, obj=wrapper), 把set_message传进来
         --> attach_wrapper(func=set_message, obj=wrapper) --> setattr(obj, func.__name__, func)
         --> 将set_message这个函数绑定到wrapper这个object instance上面，而wrapper实际上映射为add
         --> 所以add可以通过set_message去操作修改：add.set_message('Add called')
"""
