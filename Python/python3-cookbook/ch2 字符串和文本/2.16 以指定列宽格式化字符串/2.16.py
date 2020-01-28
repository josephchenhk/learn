# -*- coding: utf-8 -*-
# @Time    : 1/28/2020 2:00 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.16.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.16 以指定列宽格式化字符串

使用 textwrap 模块来格式化字符串的输出。比如，假如你有下列的长字符串：
"""

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(s, 70))
"""
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.
"""

print(textwrap.fill(s, 40))
"""
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.
"""

print(textwrap.fill(s, 40, initial_indent='    '))
"""
    Look into my eyes, look into my
eyes, the eyes, the eyes, the eyes, not
around the eyes, don't look around the
eyes, look into my eyes, you're under.
"""

print(textwrap.fill(s, 40, subsequent_indent='    '))
"""
Look into my eyes, look into my eyes,
    the eyes, the eyes, the eyes, not
    around the eyes, don't look around
    the eyes, look into my eyes, you're
    under.
"""


"""textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端大小的时候。 你可以使用 os.get_terminal_size() 方法
来获取终端的大小尺寸。比如："""

# # Sadly this part doesn't work in windows
# import os
# print(os.get_terminal_size())

