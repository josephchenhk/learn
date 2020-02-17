# -*- coding: utf-8 -*-
# @Time    : 17/2/2020 10:02 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.5.py
# @Software: PyCharm

"""
3.5 字节到大整数的打包与解包

"""

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data)) # 16
print(int.from_bytes(data, 'little')) # 69120565665751139577663547927094891008
print(int.from_bytes(data, 'big'))    # 94522842520747284487117727783387188

x = 94522842520747284487117727783387188

print(x.to_bytes(16, 'little'))  # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'
print(x.to_bytes(16, 'big'))     # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

"""如果你给出的位数不够时，将会报错"""
try:
    print(x.to_bytes(8, 'big'))
except OverflowError as e:
    print(e) # OverflowError: int too big to convert

"""要决定一个给定的整数需要多少位，可以用 int.bit_length 决定需要多少字节位来存储这个值"""
print(x.bit_length()) # 117
nbytes, rem = divmod(x.bit_length(), 8) # 一个字节8个bit
print(nbytes, rem) # 14, 5

if rem:
    nbytes += 1  # 如果还有剩余，将会需要再多一个字节才能够储存
print(nbytes) # 15

try:
    print(x.to_bytes(15, 'big')) # b'\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
except OverflowError as e:
    print(e)

try:
    print(x.to_bytes(14, 'big'))
except OverflowError as e:
    print(e)  # OverflowError: int too big to convert
