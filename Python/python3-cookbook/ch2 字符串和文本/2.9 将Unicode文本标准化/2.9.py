# -*- coding: utf-8 -*-
# @Time    : 1/23/2020 7:54 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 2.9.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
2.9 将Unicode文本标准化

在Unicode中，某些字符能够用多个合法的编码表示。为了说明，考虑下面的这个例子：
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)  # Spicy Jalapeño
print(s2)  # Spicy Jalapeño
print(s1==s2) # False

"""
这里的文本”Spicy Jalapeño”使用了两种形式来表示。 第一种使用整体字符”ñ”(U+00F1)，第二种使用拉丁字母”n”后面跟一个”~”的组合字符(U+0303)。
在需要比较字符串的程序中使用字符的多种表示会产生问题。 为了修正这个问题，你可以使用unicodedata模块先将文本标准化：
"""
import unicodedata
# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(ascii(t1), ascii(t2), (t1 == t2)) # 'Spicy Jalape\xf1o' 'Spicy Jalape\xf1o' True

# NFD表示字符应该分解为多个组合字符表示
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(ascii(t1), ascii(t2), (t1 == t2)) # 'Spicy Jalapen\u0303o' 'Spicy Jalapen\u0303o' True

"""假设你想清除掉一些文本上面的变音符的时候(可能是为了搜索和匹配)，可以用 unicodedata.combining："""
s3 = ''.join(c for c in t1 if not unicodedata.combining(c))
print(s3) # Spicy Jalapeno (去掉了n上面的小弯弯了)