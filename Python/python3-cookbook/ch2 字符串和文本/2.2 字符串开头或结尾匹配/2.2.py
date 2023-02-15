# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 11:24 AM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.2.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.2 字符串开头或结尾匹配

检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法.
注意：此方法可以传入多个匹配参数，但 *必须* 传入tuple
"""

sample_list = [
    "mystart_1.txt",
    "mystart_2.txt",
    "mystart_1.png",
    "mystart_2.png",
    "mystart_3.png",
]

print([s.startswith("mystart_1") for s in sample_list]) # [True, False, True, False, False]
print([s.endswith(".png") for s in sample_list])        # [False, False, True, True, True]

print([s.startswith(("mystart_1", "mystart_2")) for s in sample_list]) # [True, True, True, True, False]
print([s.endswith((".txt", ".png")) for s in sample_list])             # [True, True, True, True, True]

"""
也可以用re，不过小题大作了，而且也不如startswith和endswith简单明了：
"""
import re
print([True if re.match("mystart_1|mystart_2", s) else False for s in sample_list]) # [True, True, True, True, False]
