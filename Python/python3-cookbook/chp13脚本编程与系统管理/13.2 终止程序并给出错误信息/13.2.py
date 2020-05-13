# -*- coding: utf-8 -*-
# @Time    : 10/25/2019 9:16 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.2.py
# @Software: PyCharm

"""
13.2 终止程序并给出错误信息

你想向标准错误打印一条消息并返回某个非零状态码来终止程序运行
"""


# import sys
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)

# 以上自定义输出内容可以直接写在SystemExit里面：

raise SystemExit('It also failed!\n')