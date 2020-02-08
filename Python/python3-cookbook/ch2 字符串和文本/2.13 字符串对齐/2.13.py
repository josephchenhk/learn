# -*- coding: utf-8 -*-
# @Time    : 1/27/2020 6:42 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.13.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.13 字符串对齐
"""

"""对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center() 方法。比如："""
text = 'Hello World'
print(text.ljust(20))  # "Hello World         "
print(text.rjust(20))  # "         Hello World"
print(text.center(20)) # "    Hello World     "

"""也可以指定字符填充："""
print(text.ljust(20, "="))  # "Hello World========="
print(text.rjust(20, "*"))  # "*********Hello World"
print(text.center(20, "&")) # "&&&&Hello World&&&&&"

"""使用format可以达到同样的效果，你要做的就是使用 <,> 或者 ^ 字符后面紧跟一个指定的宽度。"""
print("\n使用format达到同样效果：\n")
print(format(text, "<20"))  # "Hello World         "
print(format(text, ">20"))  # "         Hello World"
print(format(text, "^20"))  # "    Hello World     "
print(format(text, "=<20"))  # "Hello World========="
print(format(text, "*>20"))  # "*********Hello World"
print(format(text, "&^20"))  # "&&&&Hello World&&&&&"

"""使用format也可以同时格式化多个值"""
print('{:=>10s} {:*>10s}'.format('Hello', 'World')) # "=====Hello *****World"
