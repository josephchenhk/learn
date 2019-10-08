# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.1.py
# @Software: PyCharm
"""
8.4 创建大量对象时节省内存方法

可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存
"""

# 不用slots
class DateWithoutSlots:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        if hasattr(self, 'hour'):
            return "Without slots: {}-{}-{}:{}".format(self.year, self.month, self.day, self.hour)
        else:
            return "Without slots: {}-{}-{}".format(self.year, self.month, self.day)


# 用slots
class DateWithSlots:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        if hasattr(self, 'hour'):
            return "With slots: {}-{}-{}:{}".format(self.year, self.month, self.day, self.hour)
        else:
            return "With slots: {}-{}-{}".format(self.year, self.month, self.day)

date_without_slots = DateWithoutSlots(2019, 6, 20)
date_with_slots = DateWithSlots(2019, 6, 20)
print(date_without_slots)
print(date_with_slots)
date_without_slots.hour = 12
print(date_without_slots)
try:
    date_with_slots.hour = 12
except AttributeError as e:
    print(e)
print(date_with_slots)

