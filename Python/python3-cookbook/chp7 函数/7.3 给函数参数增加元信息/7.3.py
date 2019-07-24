# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 7:23 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.3.py
# @Software: PyCharm
"""
7.3 给函数参数增加元信息

使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数
"""
def add(x:int, y:int) -> int:
    return x + y