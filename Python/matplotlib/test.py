# -*- coding: utf-8 -*-
# @Time    : 9/4/2021 9:27 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm
from datetime import datetime, time
import matplotlib.pyplot as plt
from matplotlib.dates import num2date
from matplotlib.ticker import Formatter
import pandas as pd
import numpy as np


data = pd.read_csv("sample.csv")

X = list(datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in data["Time"].values)
X_num = list(range(len(X)))
y = list(data["Price"].values)
"""

# 手工方法将横坐标由日期改为整数，然后创建一个对应的映射
X_num_ticks = []
X_ticks = []
for x, xn in zip(X, X_num):
    if len(X_num_ticks)>0 and (x.time()==time(9,30) and xn-X_num_ticks[-1]==1):
        X_num_ticks.pop(-1)
        X_ticks.pop(-1)
    if x.time() in [time(9,30), time(12,0), time(16,0)]:
        X_num_ticks.append(xn)
        X_ticks.append(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X_num, y, color='b')
plt.xticks(X_num_ticks, X_ticks, rotation=90)
plt.grid()
plt.show()

"""


class MyFormatter(Formatter):
    def __init__(self, X_dates):
        self.X_dates = X_dates

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(np.round(x))
        if ind >= len(self.X_dates) or ind < 0:
            return ''
        return self.X_dates[ind]


formatter = MyFormatter(X)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(formatter)
ax.plot(range(len(X)), y, color='b')
X_ticks = []
for xt, x in enumerate(X):
    if len(X_ticks)==0:
        X_ticks.append(xt)
        continue
    if len(X_ticks)>0 and (x.time()==time(9,30) and xt-X_ticks[-1]==1):
        X_ticks.pop(-1)
    if x.time() in [time(9,30), time(12,0), time(16,0)]:
        X_ticks.append(xt)

plt.xticks(X_ticks)
plt.grid()

fig.autofmt_xdate()
plt.show()
