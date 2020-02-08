# -*- coding: utf-8 -*-
# @Time    : 1/27/2020 6:55 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.14.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.14 合并拼接字符串

"""

"""如果你想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法。"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(" ".join(parts)) # Is Chicago Not Chicago?

"""最重要的需要引起注意的是，当我们使用加号(+)操作符去连接大量的字符串的时候是非常低效率的， 因为加号连接会引起内存复制以及垃圾
回收操作"""
def slow(parts, repeat=1000):
    n = 0
    while n<repeat:
        s = ''
        for p in parts:
            s += p
        n += 1
    return s

def fast(parts, repeat=1000):
    n = 0
    while n < repeat:
        s = ''.join(parts)
        n += 1
    return s

from datetime import datetime

tic = datetime.now()
s = slow(parts, repeat=100000)
toc = datetime.now()
print(f"Slow [{s}]: {(toc-tic).microseconds} microseconds.") # Slow [IsChicagoNotChicago?]: 138998 microseconds.

tic = datetime.now()
s = fast(parts, repeat=100000)
toc = datetime.now()
print(f"Fast [{s}]: {(toc-tic).microseconds} microseconds.") # Fast [IsChicagoNotChicago?]: 46100 microseconds.

"""同样还得注意不必要的字符串连接操作。有时候程序员在没有必要做连接操作的时候仍然多此一举。比如在打印的时候："""
a, b,c = "a", "b", "c"
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c]))   # Still ugly
print(a, b, c, sep=':')      # Better


"""如果你准备编写构建大量小字符串的输出代码， 你最好考虑下使用生成器函数，利用yield语句产生输出片段。比如："""
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ' '.join(sample())
print(text) # Is Chicago Not Chicago?