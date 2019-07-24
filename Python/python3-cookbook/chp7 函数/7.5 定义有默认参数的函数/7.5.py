# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 11:34 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.5.py
# @Software: PyCharm
"""
7.5 定义有默认参数的函数

定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了.
"""

def spam(a, b=42):
    print(a, b)

spam(1)    # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2