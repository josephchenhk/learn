# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 4:23 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.8 子类中扩展property.py
# @Software: PyCharm
"""
# 8.8 子类中扩展property

扩展定义在父类中的property的功能
@Parent.name.getter (好像没什么用？？)
@Parent.name.setter
"""

class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        print("[22] Original getting name.")
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        print("[28] Original setting name to {}".format(value))
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    # @Person.name.getter
    @property
    def name(self):
        print('[42] Getting name')
        return super(SubPerson, SubPerson).name

    @Person.name.setter
    def name(self, value):
        print('[47] Setting name to', value)
        # super(SubPerson, SubPerson).name.__set__(self, value)
        print(type(self), "!!")
        super(SubPerson, type(self)).name.__set__(self, value)

sp = SubPerson("Joseph")
# 先调用47行
# 再调用28行
print(sp.name)
# 先调用42行(??)
# 再调用22行

"""
** MRO **
对于你定义的每一个类，Python 会计算出一个方法解析顺序（Method Resolution Order, MRO）列表，它代表了类继承的顺序，我们
可以使用下面的方式获得某个类的 MRO 列表：

>>> C.mro()   # or C.__mro__ or C().__class__.mro()
[__main__.C, __main__.A, __main__.B, __main__.Base, object]

** super的原理 **
对super对象进行方法调用时, super(cls, inst or type)发生的事情如下:

找到第一个参数(即cls)的__mro__列表中的下一个直接定义了该方法的类, 并实例化出一个对象
然后将这个对象的self变量绑定到第二个参数上, 返回这个对象
"""
print(SubPerson.mro())
print(super(SubPerson))  # 省略第二个参数的时候返回的是未绑定的super对象
print(super(SubPerson, sp))
print(super(SubPerson, SubPerson))
print(super(SubPerson, sp)==super(SubPerson, SubPerson)) # ??
