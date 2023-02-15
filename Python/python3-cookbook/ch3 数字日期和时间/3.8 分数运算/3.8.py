# -*- coding: utf-8 -*-
# @Time    : 23/2/2020 11:43 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.8.py
# @Software: PyCharm

"""
3.8 分数运算

fractions 模块可以被用来执行包含分数的数学运算
"""
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
c = a + b
print(c) # 27/16

print(c.numerator, c.denominator) # 27 16

# Converting to a float
print(float(c)) # 1.6875

# Converting a float to a fraction
print(Fraction(*1.6875.as_integer_ratio())) # 27/16
