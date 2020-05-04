# -*- coding: utf-8 -*-
# @Time    : 27/4/2020 8:51 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: scipy_stats_sample.py
# @Software: PyCharm

class Descriptor(object):
    def __get__(self, obj, type=None):
            return 'get', self, obj, type
    def __set__(self, obj, val):
        print ('set', self, obj, val)
    def __delete__(self, obj):
        print ('delete', self, obj)


class T(object):
    # d是T的类属性，作为Descriptor的实例，它有get等方法，是一个描述符
    d = Descriptor()


t = T()# T是一个类，t是它的一个实例，d是T的一个descriptor属性
print (' t.d:', t.d) # t.d，返回的实际是d.__get__(t, T)
print (' T.d:', T.d) # T.d，返回的实际是d.__get__(None, T)，所以obj的位置为None
t.d = 'hello' # 在实例上对descriptor设置值，在__set__方法中print语句输出的。
print (' t.d:', t.d) # 可见，调用了Python调用了__set__方法，并没有改变t.d的值
T.d = 'hello' # 没有调用__set__方法
print (' T.d:', T.d)
# t.d的值也变了，这可以理解，按我们上面说的属性查找策略，t.d是从T.__dict__中得到的T.__dict__['d']的值是'hello'，t.d当然也是'hello'
print (' t.d:', t.d)


"""
data descriptor和non-data descriptor：
象上面的d，同时具有get和set方法，这样的descriptor叫做data descriptor，如果只有get方法，则叫做non-data descriptor。容易想到，由于
non-data descriptor没有set方法，所以在通过实例对属性赋值时，会直接赋值。

属性查找策略：
1.如果attr是一个Python自动产生的属性，找到！(优先级非常高！)
2.查找obj.class.dict，如果attr存在并且是data descriptor，返回data descriptor的get方法的结果，如果没有继续在obj.class的父类以及祖先类中
寻找data descriptor
3.在obj.dict中查找，这一步分两种情况，第一种情况是obj是一个普通实例，找到就直接返回，找不到进行下一步。第二种情况是obj是一个类，依次在obj和它的
父类、祖先类的dict中查找，如果找到一个descriptor就返回descriptor的get方法的结果，否则直接返回attr。如果没有找到，进行下一步。
4.在obj.class.dict中查找，如果找到了一个descriptor(插一句：这里的descriptor一定是non-data descriptor，如果它是data descriptor，第二
步就找到它了)descriptor的get方法的结果。如果找到一个普通属性，直接返回属性值。如果没找到，进行下一步。
5.很不幸，Python终于受不了。在这一步，它raise AttributeError
————————————————
版权声明：本文为CSDN博主「lilong117194」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lilong117194/java/article/details/80090951
"""

print("="*20)

class NonDataDescriptor(object):
    """只有get方法，无set方法，也无delete方法"""
    def __get__(self, obj, type=None):
            return 'get', self, obj, type


class TWithNonDataDescriptor(object):
    # d是T的类属性，作为Descriptor的实例，它有get方法，无set方法，是一个non-data描述符
    d = NonDataDescriptor()

    def __init__(self, init_d):
        # self.__dict__["d"] = init_d
        self.d = init_d

class TWithDataDescriptor(object):
    # d是T的类属性，作为Descriptor的实例，它有get方法，也有set方法，是一个data描述符
    d = Descriptor()

    def __init__(self, init_d):
        self.d = init_d

t1 = TWithNonDataDescriptor("NonDataDescriptor")# TWithNonDataDescriptor是一个类，t1是它的一个实例，d是TWithNonDataDescriptor的一个non-data descriptor属性
t2 = TWithDataDescriptor("DataDescriptor")# TWithDataDescriptor是一个类，t2是它的一个实例，d是TWithDataDescriptor的一个data descriptor属性
print (' t1.d:', t1.d) # t1.d，返回的实际是 NonDataDescriptor
print (' t2.d:', t2.d) # t2.d，返回的实际是 d.__get__(t2, TWithDataDescriptor)''

"""
>>> t.__class__.__dict__
mappingproxy({'__module__': '__main__', 'd': <__main__.NonDataDescriptor object at 0x00000001108a7948>, '__doc__': None})

>>> t.__dict__
{}
"""