# -*- coding: utf-8 -*-
# @Time    : 5/1/2022 5:08 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: sample2_test.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
