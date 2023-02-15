# -*- coding: utf-8 -*-
# @Time    : 5/1/2022 4:48 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: sample1_test.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
