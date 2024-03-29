# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 11:41 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 7.7 匿名函数捕获变量值.py
# @Software: PyCharm
"""
7.7 匿名函数捕获变量值

lambda表达式中，不作为参数传入的变量，是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的.
"""

# 错误的例子
funcs = [(lambda x: x+n) for n in range(5)]  # 这里n是一个自由变量，是运行时才绑定的
for f in funcs:
    print(f(0))   # 打出全部是4： 4 4 4 4 4, 因为真正运行时，n的取值已经是4了

print("---------------我是分割线----------------\n")
# 正确的例子
funcs = [(lambda x, n=n: x+n) for n in range(5)]  # n作为一个默认参数，随着range(5)值的变化而变化
for f in funcs:
    print(f(0))   # 打出全部是4： 0 1 2 3 4
