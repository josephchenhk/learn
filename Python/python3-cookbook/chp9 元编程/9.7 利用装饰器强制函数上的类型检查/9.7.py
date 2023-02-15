# -*- coding: utf-8 -*-
# @Time    : 7/25/2019 5:25 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.7.py
# @Software: PyCharm
"""
9.7 利用装饰器强制函数上的类型检查

作为某种编程规约，你想在对函数参数进行强制类型检查。我们的目标是实现如下功能：

"""
from functools import wraps

def typeassert(x_type, y_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x, y = args
            assert isinstance(x, x_type), "Argument x must be <class 'int'>"
            assert isinstance(y, y_type), "Argument y must be <class 'int'>"
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 一个更加general的写法
from inspect import signature
def typeassert_better(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments   # 签名绑定参数类型

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)                      # 签名绑定参数
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):          # 校验参数的类型是否合法
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate

# @typeassert(int, int)
# def add(x, y):
#     return x + y

@typeassert_better(int, int)
def add(x, y):
    return x + y


print(add(2,3))
print(add(2, 'hello'))
