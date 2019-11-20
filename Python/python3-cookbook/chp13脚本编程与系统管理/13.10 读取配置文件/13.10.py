# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 10:07 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.10.py
# @Software: PyCharm

"""
13.10 读取配置文件

怎样读取普通.ini格式的配置文件？
configparser 模块能被用来读取配置文件。
"""

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("config.ini")

print(cfg.sections())
print(cfg.get('installation','library'))
print(cfg.getboolean('debug','log_errors'))
print(cfg.getint('server','port'))
print(cfg.get('server','signature'))

cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)
print(cfg.getboolean('debug','log_errors'))
print(cfg.getint('server','port'))