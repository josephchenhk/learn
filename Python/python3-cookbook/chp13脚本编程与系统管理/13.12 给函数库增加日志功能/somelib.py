# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:05 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: somelib.py
# @Software: PyCharm

import logging

# 创建一个和调用模块同名的logger模块
log = logging.getLogger(__name__)

# 将一个空处理器绑定到刚刚已经创建好的logger对象上。 一个空处理器默认会忽略调用所有的日志消息。 因此，如果使用该函数
# 库的时候还没有配置日志，那么将不会有消息或警告出现
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')
