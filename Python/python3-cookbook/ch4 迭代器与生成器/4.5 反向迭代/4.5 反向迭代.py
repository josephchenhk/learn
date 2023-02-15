# -*- coding: utf-8 -*-
# @Time    : 1/3/2020 9:03 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.5 反向迭代.py
# @Software: PyCharm

"""
4.5 反向迭代

可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代
"""

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
