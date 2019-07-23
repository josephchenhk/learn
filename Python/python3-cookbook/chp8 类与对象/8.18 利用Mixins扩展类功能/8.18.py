# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 8:59 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.18.py
# @Software: PyCharm
"""
8.18 利用Mixins扩展类功能

利用混入类的继承关系，去扩展功能
"""

# 一个简单的混入类，提供读、增、删的日志功能
class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging.
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)

# 使用混入类去扩展dict的功能 -> 提供读、增、删的日志功能
class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23    # Setting ...
print(d['x'])  # Getting ...
del d['x']     # Deleting ...

# 直接继承、修改dict也可以吧？
class LoggedDict2(dict):
    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)

print("---------------------------\n")
d = LoggedDict2()
d['x'] = 23    # Setting ...
print(d['x'])  # Getting ...
del d['x']     # Deleting ...


