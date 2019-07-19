# -*- coding: utf-8 -*-
# @Time    : 7/19/2019 9:38 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 8.12.py
# @Software: PyCharm
"""
8.12 定义接口或者抽象基类


使用 abc 模块可以很轻松的定义抽象基类
"""

from abc import ABCMeta, abstractmethod
"""
关于metaclass，可以参看这篇文章： https://wiki.jikexueyuan.com/project/explore-python/Class/metaclass.html
"""
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