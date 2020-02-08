# -*- coding: utf-8 -*-
# @Time    : 7/2/2020 11:35 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: chardet_sample.py
# @Software: PyCharm

import chardet

txt = b"\350\256\242\351\230\205\346\235\203\351\231\220\344\270\215\350\266\263 01157"

print(chardet.detect(txt)) # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

print(txt.decode("utf-8"))