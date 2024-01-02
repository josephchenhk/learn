# -*- coding: utf-8 -*-
# @Time    : 20/8/2023 10:03 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: sample2.py

"""
Copyright (C) 2022 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the terms of the JXW license,
which unfortunately won't be written for another century.

You should have received a copy of the JXW license with this file. If not,
please write to: josephchenhk@gmail.com
"""
from functools import wraps

def my_decorator(method):
    @wraps(method)
    def wrapper(self):
        print("Before method is called")
        result = method(self)
        print("After method is called")
        return result
    return wrapper


class AutoDecoratorMeta(type):
    def __new__(cls, name, bases, attrs):
        # Check if the method is overridden in the class
        if 'func' in attrs:
            attrs['func'] = my_decorator(attrs['func'])
        return super().__new__(cls, name, bases, attrs)


class A(metaclass=AutoDecoratorMeta):
    def func(self):
        print("A's func")


class B(A):
    def func(self):
        super().func()
        print("B's func")


obj = B()
obj.func()
