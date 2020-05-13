# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:11 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.13.py
# @Software: PyCharm

"""
13.13 实现一个计时器

一般来说， 使用 time.time() 或 time.clock() 计算的时间精度因操作系统的不同会有所不同。 而使用 time.perf_counter()
函数可以确保使用系统上面最精确的计时器。
"""

import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1

# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)
t.reset() # 计时清零

# Use 2: As a context manager
with t:
    countdown(1000000)

print(t.elapsed)

with Timer() as t2:
    countdown(1000000)
print(t2.elapsed)