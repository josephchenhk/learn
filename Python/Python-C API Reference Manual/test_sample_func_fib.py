# -*- coding: utf-8 -*-
# @Time    : 30/6/2020 9:23 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample_func_fib.py
# @Software: PyCharm

from fib import fib, fib_pyobj, fib_parsearg

"""
When n is not an integer object, PyLong_AsUnsignedLong() raises an exception and returns (unsigned long) -1 which is 
UNSIGNED_LONG_MAX. We ignore the error and enter the Fibonacci function’s loop which tries computing the 
18446744073709551615th Fibonacci number which will take a very long time.
"""
# print(fib("a"))
# print(fib(9223372036854775808))  # ok
# print(fib(18446744073709551616)) # overflow if we use unsigned long
# print(fib_pyobj(18446744073709551616)) # ok if we use number protocol (PyObject *) instead of unsigned long


# print(fib(41))
# print(fib_pyobj(41))
print(fib(41)==fib_pyobj(41))

print(fib_parsearg(n=41), fib(41))
