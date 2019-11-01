# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 9:02 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.6.py
# @Software: PyCharm

"""
13.6 执行外部命令并获取它的输出

"""

import subprocess
out_bytes = subprocess.check_output(['netstat','-a'])   # This will take a huge amount of time!
out_text = out_bytes.decode('utf-8')
print(out_text)