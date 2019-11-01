# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:07 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.12.py
# @Software: PyCharm

"""
13.12 给函数库增加日志功能

你想给某个函数库增加日志功能，但是又不能影响到那些不使用日志功能的程序。
"""

import somelib

print("使用这个配置，默认情况下不会打印日志。例如：")
somelib.func()

print("不过，如果配置过日志系统，那么日志消息打印就开始生效，例如：")
import logging
logging.basicConfig()
somelib.func()