# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.1.py
# @Software: PyCharm
"""
8.5 在类中封装属性名

使用双下划线开始会导致访问名称变成其他形. 这样重命名的目的是什么，答案就是继承——这种属性通过继承是无法被覆盖的.
这里，私有名称 __private 和 __private_method 被重命名为 _C__private 和 _C__private_method ，这个跟父类B中的名称是完全不同的.
"""

class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

    def get_private(self):
        return self.__private

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass

    def get_private(self):
        return self.__private

b = B()
c = C()
print(b.get_private())  # 0
print(c.get_private())  # 1
print(b._B__private)    # 0
print(c._B__private)    # 0 (C继承B，但不会覆盖 _B__private)
print(c._C__private)    # 1