# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.1.py
# @Software: PyCharm

"""
8.1 改变对象的字符串显示

重新定义 __str__() 和 __repr__() 方法：
__str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串；
__repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例，使用交互式解释器会显示这个值
"""
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print('p is {0!r}'.format(p))  # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
print('p is {0}'.format(p))
print(eval(repr(p)) == p)