# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 2:21 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.11 随机选择.py
# @Software: PyCharm

"""
3.11 随机选择

random.choice()
"""

import random
values = [1, 2, 3, 4, 5, 6]
# 随机抽一个样品
print(random.choice(values))    # 3
# 随机抽一堆样品
print(random.sample(values, 2)) # [2, 1]

# 打乱顺序
random.shuffle(values)
print(values)                   # [1, 5, 2, 4, 6, 3]

# 生成随机整数: random.randint(a,b),范围在a到b之间
print(random.randint(0,10))     # 7

# 生成随机小数: random.random(),范围在0到1之间
print(random.random())          # 0.7894128976619269

# 如果要获取N位随机位(二进制)的整数，使用 random.getrandbits()
# 这里填3表示3位二进制的整数，表示 0 - 7之间（2^2+2^1+2^0=7)
print(random.getrandbits(3))   # 2

"""
random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子
"""
random.seed()            # Seed based on system time or os.urandom()
random.seed(12345)       # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data

"""
最后，注意在 random 模块中的函数不应该用在和密码学相关的程序中。 如果你确实需要类似的功能，可以使用ssl模块中相应的函数。 比如， 
ssl.RAND_bytes() 可以用来生成一个安全的随机字节序列。
"""