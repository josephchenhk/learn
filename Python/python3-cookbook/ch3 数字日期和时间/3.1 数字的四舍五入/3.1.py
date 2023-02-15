# -*- coding: utf-8 -*-
# @Time    : 8/2/2020 7:06 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.1.py
# @Software: PyCharm

"""
3.1 数字的四舍五入

对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可。比如：
"""

print(round(1.23, 1)) # 1.2

"""
Attention: 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2。
"""
print(round(1.5)) # 2
print(round(2.5)) # 2

"""
传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面。比如：
"""
print(round(123456, -2)) # 123500
