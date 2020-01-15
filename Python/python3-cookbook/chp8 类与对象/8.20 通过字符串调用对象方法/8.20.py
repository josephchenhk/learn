# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 9:29 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.20.py
# @Software: PyCharm
"""
8.20 通过字符串调用对象方法

你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。
方法1： getattr()
方法2： operator.methodcaller()
"""

import math
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)

# 方法 1
d = getattr(p, 'distance')(0, 0)  # Calls p.distance(0, 0)
print(d)

# 方法 2
operator.methodcaller('distance', 0, 0)(p)
print(d)
