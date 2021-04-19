# -*- coding: utf-8 -*-
# @Time    : 19/4/2021 7:44 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test.py
# @Software: PyCharm

class Test:
    def __init__(self, a={}):
        self.a = a

    def update(self):
        self.a[1] = 2


t = Test()
print(t.a)

t.update()

t2 = Test()
print(t2.a)