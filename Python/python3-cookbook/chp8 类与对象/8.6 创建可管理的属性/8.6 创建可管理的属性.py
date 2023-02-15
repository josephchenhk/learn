# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.6 创建可管理的属性.py
# @Software: PyCharm
"""
8.6 创建可管理的属性

上述代码中有三个相关联的方法，这三个方法的名字都必须一样。 第一个方法是一个 getter 函数，它使得 first_name 成为一个属性。
其他两个方法给 first_name 属性添加了 setter 和 deleter 函数。 需要强调的是只有在 first_name 属性被创建后， 后面的两个
装饰器 @first_name.setter 和 @first_name.deleter 才能被定义。
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name # 这里会调用setter，将值传给self._first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string, but got a {} value: {}'.format(type(value), value))
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

p = Person("Joseph")
print(p.first_name)

try:
    p.first_name = 30
except TypeError as e:
    print(e)

try:
    del p.first_name
except AttributeError as e:
    print(e)
