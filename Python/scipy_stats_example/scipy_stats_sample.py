# -*- coding: utf-8 -*-
# @Time    : 3/5/2020 12:32 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: scipy_stats_sample.py
# @Software: PyCharm

"""
scipy.stats

有一些通用的概率分布类被封装在continuous random variables以及 discrete random variables中。有80多个连续性随机变量(RVs)以及10余个离散随
机变量已经用 这些类建立。

让我们使用一个标准正态(normal)随机变量(RV)作为例子。
连续随机变量的主要公共方法如下：

rvs:随机变量（就是从这个分布中抽一些样本）
pdf：概率密度函数。
cdf：累计分布函数
sf：残存函数（1-CDF）
ppf：分位点函数（CDF的逆）
isf：逆残存函数（sf的逆）
stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
moment:分布的非中心矩。
"""
from scipy.stats import norm
print(norm.cdf(0.))           # 0.5
print(norm.cdf([-1., 0, 1]))  # [0.15865525 0.5        0.84134475]
print(norm.ppf(0.5))                            # 0.0
print(norm.ppf([0.15865525, 0.5, 0.84134475]))  # [-1.00000002  0.          1.00000002]

import matplotlib.pyplot as plt
import scipy
import scipy.stats
size = 20000
x = scipy.arange(size)
# creating the dummy sample (using beta distribution)
y = scipy.int_(scipy.round_(scipy.stats.beta.rvs(6,2,size=size)*47))
# creating the histogram
h = plt.hist(y, bins=range(48))

dist_names = ['alpha', 'beta']#, 'arcsine',
              # 'weibull_min', 'weibull_max', 'rayleigh']

for dist_name in dist_names:
    dist = getattr(scipy.stats, dist_name)
    param = dist.fit(y)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
    plt.plot(pdf_fitted, label=dist_name)
    plt.xlim(0,47)
plt.legend(loc='upper left')
plt.show()
