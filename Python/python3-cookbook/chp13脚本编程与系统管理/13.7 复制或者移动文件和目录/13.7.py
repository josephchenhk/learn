# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 9:18 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.7.py
# @Software: PyCharm

"""
13.7 复制或者移动文件和目录

你想要复制或移动文件和目录，但是又不想调用shell命令
shutil 模块有很多便捷的函数可以复制文件和目录。使用起来非常简单
"""

import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)
