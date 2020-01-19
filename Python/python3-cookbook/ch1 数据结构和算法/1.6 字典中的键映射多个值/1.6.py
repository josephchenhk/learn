# -*- coding: utf-8 -*-
# @Time    : 1/17/2020 3:05 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.6.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.6 字典中的键映射多个值

通常字典里一个key对应一个value，当value是一个列表或object时，便可以包含多个值的信息

普通的字典如果key不存在，尝试赋值时会报错；但是用defaultdict就不会有这样的问题
"""

normal_dict = {'a':[]}
normal_dict['a'].append(1)
print(normal_dict) # >> {'a': [1]}

try:
    normal_dict['b'].append(2)
except KeyError as e:
    print(f"Error! {e}")  # >> KeyError: 'b'

from collections import defaultdict
default_dict = defaultdict(list) # list means value type is list
default_dict['b'].append(2)
print(default_dict) # >> defaultdict(<class 'list'>, {'b': [2]})
print(default_dict['b']) # >> [2]