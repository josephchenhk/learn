# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 4:11 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 7.11 内联回调函数.py
# @Software: PyCharm
"""
7.11 内联回调函数

其实我还是看不懂这个复杂的流程意义所在
"""

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello ', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

# test()

if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    # Run the test function
    test()

"""
解释：
test() = inlined_async(test)() --> wrapper(): f = func(*args) -->test() --> Async(add, (2, 3))
         --> 执行到yield之前一句，暂停，返回生成器给f --> result_queue = Queue(), result_queue.put(None) 
         --> result = result_queue.get() --> result=None --> a = f.send(result) --> 把None发送给generator f
         --> f从上一次yield停止那里开始resume，将Async(add, (2, 3))作为return返回给a --> a=Async(add, (2, 3))
         --> apply_async(a.func, a.args, callback=result_queue.put) --> 执行2+3=5，然后将5放入result_queue
         --> result_queue.put(5) --> 现在result_queue又有内容了，继续跑在while True循环 --> result = result_queue.get()
         --> result = 5 --> a = f.send(result) --> 把5发送给generator f --> f继续向下执行 --> 把5赋值给r
         --> 执行print(r) --> 打印出5 --> ...
"""