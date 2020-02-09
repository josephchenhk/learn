# -*- coding: utf-8 -*-
# @Time    : 8/2/2020 7:14 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.2.py
# @Software: PyCharm

"""
3.2 执行精确的浮点数运算

如果你想更加精确(并能容忍一定的性能损耗)，你可以使用 decimal 模块：
"""

from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a+b) # 6.3

print((a+b)==Decimal(6.3)) # False???

"""
decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。 为了这样做，你先得创建一个本地上下文并更改它的设置，比如：
"""

from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print(a/b) # 0.7647058823529411764705882353

with localcontext() as ctx:
    ctx.prec = 5
    print(a/b) # 0.76471

"""
用原生的浮点数是速度更快的，在不是对精度要求非常高的时候，用原生浮点数更好；但也要注意，原生浮点数的误差有的时候不可忽略，例如：
"""

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums)) # 0.0 (注意这里的1不见了)

import math
print(math.fsum(nums)) # 1.0


