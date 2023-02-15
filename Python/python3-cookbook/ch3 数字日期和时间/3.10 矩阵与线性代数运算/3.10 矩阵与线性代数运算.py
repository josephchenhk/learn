# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 2:07 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.10 矩阵与线性代数运算.py
# @Software: PyCharm

"""
3.10 矩阵与线性代数运算

numpy.matrix
"""

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])

print(m)
print(m.T)  # transpose
print(m.I)  # inverse

"""
Create a vector and multiply

m*v =
    _           _   _   _   _   _
    | 1  -2   3 |   | 2 |   | 8 |
    | 0   4   5 | * | 3 | = |32 |
    | 7   9  -9 |   | 4 |   | 2 |
    -           -   -   -   -   -
"""
v = np.matrix([[2],[3],[4]])
print(m*v)


"""
可以在 numpy.linalg 子包中找到更多的操作函数
"""
# Determinant
print(np.linalg.det(m))      # -229.99999999999983


# Eigenvalues
print(np.linalg.eigvals(m))  # [-13.11474312   2.75956154   6.35518158]


# Solve for x in mx = v
x = np.linalg.solve(m, v)
print(m*x)                   # np.matrix([[2],[3],[4]])
