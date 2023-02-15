# -*- coding: utf-8 -*-
# @Time    : 23/2/2020 11:39 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.7 无穷大与NaN.py
# @Software: PyCharm

"""
3.7 无穷大与NaN

Python并没有特殊的语法来创建或测试正无穷、负无穷或NaN(非数字)的浮点数，但是可以使用 float() 来创建它们
"""

a = float('inf')
b = float('-inf')
c = float('nan')

import math
print(math.isinf(a)) # True
print(math.isinf(b)) # True
print(math.isnan(c)) # True
