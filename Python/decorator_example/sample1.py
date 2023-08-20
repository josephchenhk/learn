# -*- coding: utf-8 -*-
# @Time    : 20/8/2023 8:43 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: sample1.py

"""
Copyright (C) 2022 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the terms of the JXW license,
which unfortunately won't be written for another century.

You should have received a copy of the JXW license with this file. If not,
please write to: josephchenhk@gmail.com
"""

def uppercase_decorator(method):
    def wrapper(cls, text):
        result = method(cls, text.upper())
        return result

    return wrapper


class TextProcessor:
    @classmethod
    @uppercase_decorator
    def process_text(cls, text):
        print("Processing text:", text)
        return len(text)


text = "hello, world!"
result = TextProcessor.process_text(text)
print("Result:", result)
