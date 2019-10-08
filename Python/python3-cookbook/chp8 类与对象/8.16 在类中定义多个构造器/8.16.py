# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 6:20 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.16.py
# @Software: PyCharm
"""
8.16 在类中定义多个构造器

想实现一个类，除了使用 __init__() 方法外，还有其他方式可以初始化它。例如：使用到类方法
"""

import time

class Date:
    """方法一：使用类方法"""
    # Primary constructor （一定要实现）
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor （只有实现了primary constructor之后，才可以使用）
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)

    __repr__ = __str__

a = Date(2012, 12, 21) # Primary
b = Date.today()       # Alternate
print(a)
print(b)