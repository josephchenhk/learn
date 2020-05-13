# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 2:55 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 7.10 带额外状态信息的回调函数.py
# @Software: PyCharm
"""
7.10 带额外状态信息的回调函数

你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)， 并且你还需要让回调函数拥有额外的
状态值，以便在它的内部使用到。
"""

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

# 一个小例子
def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2,3), callback=print_result)

"""
重点来了！

为了让回调函数访问外部信息，有三种方法。

第一种方法是使用一个绑定方法来代替一个简单函数。 比如，下面这个类会保存一个内部序列号，每次接收到一个 result 的时候
序列号加1；使用这个类的时候，你先创建一个类的实例，然后用它的 handler() 绑定方法来做为回调函数。
"""
print("-----------------我是无情的分割线------------------\n")
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

print("\n第一种方法（类方法）：")
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)               # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=r.handler)   # [2] Got: helloworld

"""
第二种方式，作为类的替代，可以使用一个闭包捕获状态值，例如：
"""
def make_handler():
    sequence = 0  # 初始化sequence值为0，后面每次调用handler时+1
    def handler(result):
        """Python有四类作用域（Scope）。

            局部（Local）作用域）
            封闭（Enclosing）作用域
            全局（Global）作用域
            内置（Built-in）作用域

        在作用域中按名称去寻找对象（Python中一切皆对象）时，会按照LEGB规则去查找。
        修改Global变量的问题，可以用global关键字来解决； 修改Enclosing变量的问题，就需要使用nonlocal关键字
        """
        nonlocal sequence # nonlocal用于修改enclosing作用域的变量，常用语闭包的方法
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

print("\n第二种方法（闭包方法）：")
m = make_handler()
apply_async(add, (2, 3), callback=m)               # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=m)   # [2] Got: helloworld


"""
第三种方式，更加高级，使用协程：
"""
def make_handler():
    sequence = 0
    while True:
        result = yield sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

print("\n第三种方法（协程coroutine）：")
m_co = make_handler()
m_co.send(None)   # 或者 next(handler) # Advance to the yield
# 调用send将参数传递给result
apply_async(add, (2, 3), callback=m_co.send)               # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=m_co.send)   # [2] Got: helloworld
