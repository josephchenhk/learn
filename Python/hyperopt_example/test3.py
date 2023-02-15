# -*- coding: utf-8 -*-
# @Time    : 26/8/2022 3:07 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test3.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

from hyperopt import hp
space = hp.choice('a',
    [
        ('case 1', 1 + hp.lognormal('c1', 0, 1)),
        ('case 2', hp.uniform('c2', -10, 10)),
        ('case 3', hp.uniform('c2', -10, 10))
    ])

import hyperopt.pyll.stochastic
case1 = 0
N = 10000
for _ in range(N):
    res = hyperopt.pyll.stochastic.sample(space)
    if res[0] == "case 1":
        case1 += 1
case1_ratio = float(case1) / N
print(f"case 1 ratio: {case1_ratio}")
print()
