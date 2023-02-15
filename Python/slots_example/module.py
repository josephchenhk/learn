# -*- coding: utf-8 -*-
# @Time    : 5/1/2022 11:27 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: module.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

class A(object):
    # some class a user should import
    __slots__ = ('x', 'b')

    def __init__(self):
        self.b = B()

class B(object):
    # let's suppose we can't use it directly,
    # it's returned as a part of another class
    __slots__ = ('z',)
