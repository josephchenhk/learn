# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 5:35 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 9.2 创建装饰器时保留函数元信息.py
# @Software: PyCharm
"""
9.2 创建装饰器时保留函数元信息

你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。
任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数。
"""
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    # @wraps(func) # no wraps, will lose information
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    """Counts down"""
    while n > 0:
        n -= 1

print("""没有wraps，元信息将会丢失""")
countdown(100000)                # countdown 0.012363195419311523
print(countdown.__name__)        # wrapper
print(countdown.__doc__)         # None
print(countdown.__annotations__) # {}

def timethis2(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis2
def countdown2(n:int):
    """Counts down 2"""
    while n > 0:
        n -= 1

print("""有wraps，元信息将会保留""")
countdown2(100000)                 # countdown2 0.012204170227050781
print(countdown2.__name__)         # countdown2
print(countdown2.__doc__)          # Counts down 2
print(countdown2.__annotations__)  # {'n': <class 'int'>}


print("""有wraps之后，可以通过 __wrapped__ 直接访问被包装函数""")
countdown2.__wrapped__(100000)     # 无任何print
