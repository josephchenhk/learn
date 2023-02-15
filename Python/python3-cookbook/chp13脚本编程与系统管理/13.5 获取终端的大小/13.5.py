# -*- coding: utf-8 -*-
# @Time    : 10/31/2019 4:39 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.5.py
# @Software: PyCharm

"""
13.5 获取终端的大小

"""

import os

sz = os.get_terminal_size()
print(sz, sz.columns, sz.lines)
