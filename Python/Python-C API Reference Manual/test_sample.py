# -*- coding: utf-8 -*-
# @Time    : 3/6/2020 5:53 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample.py
# @Software: PyCharm

from sample import *
# spam_system, print_function, add_function, func1_function, func2_function, func3

# print(spam_system("ls -l"))
# print(print_function())
# print(add_function(2, 4))
# print(func1_function(1, "hello", (3,4)))
# print(func1_function(1, "hello", (3,4), 50))
# print(func2_function(1))
# print(func2_function(3, state="happy", action="sing", type="red bird"))
print(func3(int, (1.234, )))
print(func3(eval, ("2+3.1", )))