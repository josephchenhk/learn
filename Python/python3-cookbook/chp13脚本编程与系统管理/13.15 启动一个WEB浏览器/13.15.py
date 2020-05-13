# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:27 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.15.py
# @Software: PyCharm

"""
13.15 启动一个WEB浏览器

想通过脚本启动浏览器并打开指定的URL网页
webbrowser 模块能被用来启动一个浏览器，并且与平台无关。例如：
"""

import webbrowser
# webbrowser.open('http://www.python.org')
#
# webbrowser.open_new('http://www.python.org')
# webbrowser.open_new_tab('http://www.python.org')

c = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')  # interesting appendix %s: why???
c.open('http://www.python.org')