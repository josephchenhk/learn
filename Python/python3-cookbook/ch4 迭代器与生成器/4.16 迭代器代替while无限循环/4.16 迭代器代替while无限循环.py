# -*- coding: utf-8 -*-
# @Time    : 8/5/2020 8:56 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.16 迭代器代替while无限循环.py
# @Software: PyCharm

"""
4.16 迭代器代替while无限循环

问题
你在代码中使用 while 循环来迭代处理数据，因为它需要调用某个函数或者和一般迭代模式不同的测试条件。 能不能用迭代器来重写这个循环呢？
"""

# while
def while_reader(s):
    while True:
        data = next(s)
        if data == b'':
            break
        print(data)

sample = [1, 2, "Hello", b""]
sample_iter = iter(sample)

while_reader(sample_iter)

# iter
def iter_reader(s):
    for data in iter(lambda:next(s), b''):
        print(data)

sample_iter = iter(sample)
iter_reader(sample_iter)

"""关于callable"""

class CallableObj:
    test_str = "hahaha"

    def __call__(self, *args, **kwargs):
        return self.test_str

print("CallableObj is callable: ", callable(CallableObj))
callable_obj = CallableObj()
print("CallableObj instance is callable(because it realized __call__): ", callable(callable_obj))
print("call result: ", callable_obj())
# 不停call callable_obj，直到遇到"hahaha"为止
for chunk in iter(callable_obj,"hahaha"):
    print(chunk)
