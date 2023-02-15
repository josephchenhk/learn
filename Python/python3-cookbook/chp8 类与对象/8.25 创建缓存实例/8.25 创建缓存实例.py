# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 6:44 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.25 创建缓存实例.py
# @Software: PyCharm
"""
8.25 创建缓存实例

在创建一个类的对象时，如果之前使用同样参数创建过这个对象， 你想返回它的缓存引用。
这种通常是因为你希望相同参数创建的对象时单例的。 在很多库中都有实际的例子，比如 logging 模块，使用相同的名称创建的
logger 实例永远只有一个。
"""

# The class in question
class Spam:
    def __init__(self, name):
        self.name = name

# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()
def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a = get_spam('foo')
b = get_spam('bar')
print("a is b: ", a is b)
c = get_spam('foo')
print("a is c: ", a is c)

"""以下方法不是一个好方法，因为每次都需要 __init__ 一次"""
# Note: This code doesn't quite work
import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self
    def __init__(self, name):
        print('Initializing Spam')
        self.name = name

print("-----------我是分割线 1--------------\n")
s = Spam('Dave')  # 会调用__init__，打印出 Initializing Spam
t = Spam('Dave')  # 会调用__init__，打印出 Initializing Spam
print("s is t: ", s is t)

"""以上方法暴露了 __init__ 给用户，可以禁用这个方法，而将实例化交给另外一个函数 _new"""

class SpamManager:
    _spam_cache = weakref.WeakValueDictionary()

    @staticmethod
    def get_spam(name):
        if name in _spam_cache:
            return _spam_cache[name]
        else:
            spam = Spam2._new(name)
            _spam_cache[name] = spam
            return spam

class Spam2:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

print("-----------我是分割线 2--------------\n")
s = SpamManager.get_spam('Dave')  # 会调用__init__，打印出 Initializing Spam
t = SpamManager.get_spam('Dave')  # 会调用__init__，打印出 Initializing Spam
print("s is t: ", s is t)
