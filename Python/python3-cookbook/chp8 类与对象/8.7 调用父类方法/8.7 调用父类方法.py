# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.7 调用父类方法.py
# @Software: PyCharm
"""
8.7 调用父类方法

为了调用父类(超类)的一个方法，可以使用 super() 函数
"""

class A:
    Ax = 9
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()  # super()相当于A，不是A()!
        self.y = 1

    def what_is_super(self):
        print(super().Ax)  # super()相当于A，不是A()! 所以调用super().x会报错


a = A()
b = B()
print(a.x)
print(f"{b.x}, {b.y}")
b.what_is_super()
