# -*- coding: utf-8 -*-
# @Time    : 30/6/2020 9:23 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample_func_fib.py
# @Software: PyCharm

from fib import fib

"""
When n is not an integer object, PyLong_AsUnsignedLong() raises an exception and returns (unsigned long) -1 which is 
UNSIGNED_LONG_MAX. We ignore the error and enter the Fibonacci function’s loop which tries computing the 
18446744073709551615th Fibonacci number which will take a very long time.
"""
print(fib("a"))