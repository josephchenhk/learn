# -*- coding: utf-8 -*-
# @Time    : 15/2/2020 11:30 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.4.py
# @Software: PyCharm

"""
3.4 二八十六进制整数

"""

"""
为了将整数转换为二进制、八进制或十六进制的文本串， 可以分别使用 bin() , oct() 或 hex() 函数
"""
x = 1234
print(bin(x))  # 0b10011010010
print(oct(x))  # 0o2322
print(hex(x))  # 0x4d2

"""
如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数。比如：
"""
print(format(x, 'b'))  # 10011010010
print(format(x, 'o'))  # 2322
print(format(x, 'x'))  # 4d2

"""
整数是有符号的，所以如果你在处理负数的话，输出结果会包含一个负号。比如：
"""
y = -1234
print(format(y, 'b'))  # -10011010010
print(format(y, 'o'))  # -2322
print(format(y, 'x'))  # -4d2

"""
如果你想产生一个无符号值，你需要增加一个指示最大位长度的值。比如为了显示32位的值，可以像下面这样写：
"""
print(format(2**32 + x, 'b'))  # 100000000000000000000010011010010
print(format(2**32 + x, 'o'))  # 40000002322
print(format(2**32 + x, 'x'))  # 1000004d2

"""
为了以不同的进制转换整数字符串，简单的使用带有进制的 int() 函数即可：
"""
print(int('10011010010', 2))  # 1234
print(int('2322', 8))         # 1234
print(int('4d2', 16))         # 1234

"""
最后，使用八进制的程序员有一点需要注意下。 Python指定八进制数的语法跟其他语言稍有不同。比如，如果你像下面这样指定八进制，会出现语法错误

>>> import os
>>> os.chmod('script.py', 0755)
    File "<stdin>", line 1
        os.chmod('script.py', 0755)
                            ^
SyntaxError: invalid token
>>>

需确保八进制数的前缀是 0o ，就像下面这样：

>>> os.chmod('script.py', 0o755)

"""
