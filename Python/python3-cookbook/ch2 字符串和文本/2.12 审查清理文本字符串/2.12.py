# -*- coding: utf-8 -*-
# @Time    : 1/25/2020 8:38 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.12.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.12 审查清理文本字符串

先创建一个小的转换表格然后使用 str.translate() 方法
"""

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s) # pýtĥöñis	awesome

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None # Deleted
}

a = s.translate(remap)
print(a) # pýtĥöñ is awesome

"""
你可以以这个表格为基础进一步构建更大的表格。比如，让我们删除所有的和音符:
"""
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b) # pýtĥöñ is awesome
print(b.translate(cmb_chrs)) # python is awesome

"""
另一种清理文本的技术涉及到I/O解码与编码函数。这里的思路是先对文本做一些初步的清理， 然后再结合 encode() 或者 decode() 操作来
清除或修改它。比如：
"""
print(b.encode('ascii', 'ignore').decode('ascii')) # python is awesome