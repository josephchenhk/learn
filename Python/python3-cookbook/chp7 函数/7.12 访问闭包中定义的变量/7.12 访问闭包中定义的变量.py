# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:14 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.12 访问闭包中定义的变量.py
# @Software: PyCharm
"""
7.12 访问闭包中定义的变量

你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。
通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。 但是，你可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这
个目的。例如：
"""

def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()               # n= 0
f.set_n(10)
f()               # n= 10
print(f.get_n())  # 10

print("---------------我是无情的分隔线---------------\n")
import sys
print(sys._getframe(1).f_locals)
