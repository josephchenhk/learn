# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 9:38 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.12 定义接口或者抽象基类.py
# @Software: PyCharm
"""
8.12 定义接口或者抽象基类


使用 abc 模块可以很轻松的定义抽象基类
"""

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

"""
抽象类的一个特点是它不能直接被实例化，比如你想像下面这样做是不行的：
a = IStream() # TypeError: Can't instantiate abstract class
                # IStream with abstract methods read, write
"""

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

ss = SocketStream()
print(ss)

"""
关于metaclass，可以参看这篇文章： https://wiki.jikexueyuan.com/project/explore-python/Class/metaclass.html'

在python 3，指示在创建Foo类时使用元类PrefixMetaclass：
class Foo(metaclass=PrefixMetaclass):

在python 2，则需在 Foo 中加一个 __metaclass__ 的属性：
class Foo(object):
    __metaclass__ = PrefixMetaclass

__new__(cls, name, bases, attrs) 是在 __init__ 之前被调用的特殊方法，它用来创建对象并返回创建后的对象，对它的参数解释如下：
cls：当前准备创建的类
name：类的名字
bases：类的父类集合
attrs：类的属性和方法，是一个字典
"""

class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        _attrs = {"my_"+k:v for k,v in attrs.items()}  # 在所有属性前面加上前缀 my_
        _attrs["echo"] = lambda self,x:x               # 加上一个叫echo的函数
        return type.__new__(cls, name, bases, _attrs)

class Foo(metaclass=PrefixMetaclass):
    name = "foo"
    def func(self):
        pass

foo = Foo()
print(foo.my_name)    # foo
print(foo.echo("hi")) # hi
