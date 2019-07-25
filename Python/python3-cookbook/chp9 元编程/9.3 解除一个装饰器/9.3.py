# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:50 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 9.3.py
# @Software: PyCharm
"""
9.3 解除一个装饰器

一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。

可以通过访问 __wrapped__ 属性来访问原始函数
"""
from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

print(add(2, 3))
print("----------------我是无耻的分割线 1---------------\n")
print(add.__wrapped__(2, 3))               # 只解除了decorator1
print("----------------我是无耻的分割线 2---------------\n")
print(add.__wrapped__.__wrapped__(2, 3))   # 解除了decorator1 和 decorator2