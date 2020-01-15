# -*- coding: utf-8 -*-
# @Time    : 10/25/2019 9:12 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.1.py
# @Software: PyCharm

"""
13.1 通过重定向/管道/文件接受输入

你希望你的脚本接受任何用户认为最简单的输入方式。包括将命令行的输出通过管道传递给该脚本、 重定向文件到该脚本，或在
命令行中传递一个文件名或文件名列表给该脚本
"""

import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line + "-hahaha\n", end='')