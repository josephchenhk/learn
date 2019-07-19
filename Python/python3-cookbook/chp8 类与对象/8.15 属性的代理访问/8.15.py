# -*- coding: utf-8 -*-
# @Time    : 6/24/2019 12:10 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.15.py
# @Software: PyCharm

# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # 调用 p._private_x 会进入这里
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

class Spam:
    def __init__(self, x):
        self.x = x
        self._private_x = "private_variable"

    def bar(self, y):
        print('Spam.bar:', self.x, y)

s = Spam(2)
p = Proxy(s)  # p is the proxy of Spam(2). It can access all public attributes in Spam(2)
print(p.x)
print(p.bar(3))
p.z = "abc"
print(p.z)
print(p._private_x)
p._private_x = "p_private_variable"
print(p._private_x)
print("Done.")