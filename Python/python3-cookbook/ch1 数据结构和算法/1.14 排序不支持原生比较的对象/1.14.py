# -*- coding: utf-8 -*-
# @Time    : 1/21/2020 5:41 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.14.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.14 排序不支持原生比较的对象

你想排序类型相同的对象，但是他们不支持原生的比较操作。可以用operator.attrgetter 或者lambda，前者更快，且支持多字段进行比较
"""


class User:
    def __init__(self, user_name, user_age):
        self.user_name = user_name
        self.user_age = user_age

    def __repr__(self):
        return f"User[{self.user_name},{self.user_age}]"


users = [User("Gamma", 23),
         User("Beta", 3),
         User("Beta", 4),
         User("Alpha", 99)
         ]

from operator import attrgetter

# 按年龄排序
print(sorted(users, key=attrgetter('user_age'))) # [User[Beta,3], User[Beta,4], User[Gamma,23], User[Alpha,99]]

# 先按姓名，再按年龄排序
print(sorted(users, key=attrgetter('user_name','user_age'))) # [User[Alpha,99], User[Beta,3], User[Beta,4], User[Gamma,23]]
