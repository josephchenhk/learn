# -*- coding: utf-8 -*-
# @Time    : 1/6/2020 11:54 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample3.py.py
# @Software: PyCharm

import sample
import array
print(sample.avg(array.array('d',[1,2,3])))

import numpy
print(sample.avg(numpy.array([1.0,2.0,3.0])))

# print(sample.avg([1.0,2.0,3.0])) # not supported

# print(sample.avg((1.0,2.0,3.0))) # not supported