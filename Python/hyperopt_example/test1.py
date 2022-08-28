# -*- coding: utf-8 -*-
# @Time    : 23/8/2022 3:38 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the 
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""
from hyperopt import fmin, tpe, hp
best = fmin(fn=lambda x: x ** 2,
    space=hp.uniform('x', -10, 10),
    algo=tpe.suggest,
    max_evals=1000)
print(best)