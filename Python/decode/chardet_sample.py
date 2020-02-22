# -*- coding: utf-8 -*-
# @Time    : 7/2/2020 11:35 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: chardet_sample.py
# @Software: PyCharm

import chardet

txt = b"\350\256\242\351\230\205\346\235\203\351\231\220\344\270\215\350\266\263 01157"

txt = b"\346\227\266\351\227\264\345\255\227\347\254\246\344\270\262\346\240\274\345\274\217\351\224\231\350\257\257"

txt = b"\346\255\244\346\225\260\346\215\256\346\232\202\346\227\266\350\277\230\346\234\252\345\207\206\345\244\207\345\245\275"

print(chardet.detect(txt)) # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

print(txt.decode("utf-8"))