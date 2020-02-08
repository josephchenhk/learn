# -*- coding: utf-8 -*-
# @Time    : 1/28/2020 2:08 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.17.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.17 在字符串中处理html和xml

你想将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本。 再者，你需要转换文本中特定的字符(比如<, >, 或 &)。
"""

s = 'Elements are written as "<tag>text</tag>".'
print(s) # lements are written as "<tag>text</tag>".

import html
print(html.escape(s)) # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.
print(html.escape(s, quote=False)) # Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

"""如果你正在处理的是ASCII文本，并且想将非ASCII文本对应的编码实体嵌入进去， 可以给某些I/O函数传递参数 
errors='xmlcharrefreplace' 来达到这个目。比如："""
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace')) # b'Spicy Jalape&#241;o'
print(s.encode('utf-8', errors='xmlcharrefreplace')) # b'Spicy Jalape\xc3\xb1o'

"""如果你接收到了一些含有编码值的原始文本，需要手动去做替换， 通常你只需要使用HTML或者XML解析器的一些相关工具函数/方法即可。
比如："""
s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s)) # Spicy "Jalapeño".

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t)) # The prompt is >>>