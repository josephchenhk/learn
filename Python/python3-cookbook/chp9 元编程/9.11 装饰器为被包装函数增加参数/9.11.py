# -*- coding: utf-8 -*-
# @Time    : 9/11/2019 10:51 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.11.py
# @Software: PyCharm

"""
9.11 装饰器为被包装函数增加参数


"""

from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper

@optional_debug
def spam(a,b,c):
    print(a,b,c)

spam(1,2,3)

spam(1,2,3,debug=True)