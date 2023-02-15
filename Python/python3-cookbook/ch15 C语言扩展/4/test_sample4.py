# -*- coding: utf-8 -*-
# @Time    : 1/6/2020 11:54 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample3.py.py
# @Software: PyCharm

import sample

data = [1, 3, 4]
sample.consume_iterable(data)


p1 = sample.Point(2,3)
p2 = sample.Point(4,5)

print(p1)
print(p2)
print(sample.mydistance(p1,p2))
