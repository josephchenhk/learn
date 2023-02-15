# -*- coding: utf-8 -*-
# @Time    : 23/2/2020 11:50 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.9.py
# @Software: PyCharm

"""
3.9 大型数组运算

用numpy
"""

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)  # [2 4 6 8]
print(ax + ay) # [ 6  8 10 12]
print(ax * ay) # [ 5 12 21 32]

"""
底层实现中， NumPy 数组使用了C或者Fortran语言的机制分配内存。 也就是说，它们是一个非常大的连续的并由同类型数据组成的内存区域。 所以，你可以构造
一个比普通Python列表大的多的数组。 比如，如果你想构造一个10,000*10,000的浮点数二维网格，很轻松：
"""
grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)

# [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  ...
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]]
