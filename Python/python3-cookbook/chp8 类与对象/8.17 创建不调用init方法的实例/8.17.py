# -*- coding: utf-8 -*-
# @Time    : 6/24/2019 2:16 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.17.py
# @Software: PyCharm
"""
8.17 创建不调用init方法的实例

你想创建一个实例，但是希望绕过执行 __init__() 方法，可以通过 __new__() 方法创建一个未初始化的实例：
__new__(输入：类)： 返回：实例

当我们在反序列对象或者实现某个类方法构造函数时需要绕过 __init__() 方法来创建对象。
"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)  # d是一个实例了
print(d)
try:
    print(d.year)
except AttributeError as e:
    print("实例还没有year这个变量：", e)

# 手工给d实例加上以下attributes
data = {'year':2012, 'month':8, 'day':29}
for key, value in data.items():
    setattr(d, key, value)
try:
    print(d.year)
except AttributeError as e:
    print("实例还没有year这个变量：", e)