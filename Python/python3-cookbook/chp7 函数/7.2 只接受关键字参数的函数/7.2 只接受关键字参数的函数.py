# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 7:18 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 7.2 只接受关键字参数的函数.py
# @Software: PyCharm
"""
7.2 只接受关键字参数的函数

将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果
"""

def recv(maxsize, *, block):
    'Receives a message'
    pass

try:
    recv(1024, True)        # TypeError
except TypeError as e:
    print(e)
recv(1024, block=True)      # Ok