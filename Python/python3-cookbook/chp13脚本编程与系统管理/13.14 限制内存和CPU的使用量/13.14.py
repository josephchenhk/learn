# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:21 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.14.py
# @Software: PyCharm

"""
13.14 限制内存和CPU的使用量

你想对在Unix系统上面运行的程序设置内存或CPU的使用限制。
resource 模块能同时执行这两个任务

(注意：需要注意的是本节内容只能适用于Unix系统，并且不保证所有系统都能如期工作。 比如我们在测试的时候，它能在Linux上面
正常运行，但是在OS X上却不能。)
"""

import signal
import resource # In Windows, ModuleNotFoundError: No module named 'resource'
import os

def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)

def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

if __name__ == '__main__':
    set_max_runtime(5)
    while True:
        pass
