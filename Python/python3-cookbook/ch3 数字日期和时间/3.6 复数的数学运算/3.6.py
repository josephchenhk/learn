# -*- coding: utf-8 -*-
# @Time    : 22/2/2020 8:51 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.6.py
# @Software: PyCharm

"""
3.6 复数的数学运算

"""

"""
复数在python的两种表达
"""
a = complex(1, 2)
b = 3 + 4j
c = a + b
print(c) # (4+6j)

"""
对应的实部、虚部和共轭复数可以很容易的获取
"""
print(c.real, c.imag, c.conjugate()) # 4.0 6.0 (4-6j)

"""
如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
"""
import cmath
print(cmath.sin(c))  # (-152.65889676010067-131.84851855934087j)
print(cmath.cos(c))  # (-131.85013877988885+152.6570208342681j)
print(cmath.sqrt(c)) # (2.3676045437243083+1.2671034983236331j)
