# -*- coding: utf-8 -*-
# @Time    : 19/4/2021 7:44 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm

class Test:
    def __init__(self, a=dict()):
        self.a = a

    def add(self, k, v):
        self.a[k] = v

# class Test:
#     def __init__(self, a=list()):
#         self.a = a
#
#     def add(self):
#         self.a.append(2)

# class Test:
#     def __init__(self, a=0):
#         self.a = a
#
#     def add(self):
#         self.a += 1

t1 = Test()
print(t1.a)

t1.add(1,2)

t2 = Test()
print(t2.a)

t2.add(3,4)

t3 = Test()
print(t3.a)

"""
Ref: https://blog.csdn.net/dpengwang/article/details/100128420

当list ， dict等可变类型作为默认参数时，只会在定义函数的时候执行一次，有点像静态变量，定义一次后面一直使用。在之后使用函数的过程中，如果没有对默认
参数进行赋值，那么将会一直使用这个初始的变量。
"""