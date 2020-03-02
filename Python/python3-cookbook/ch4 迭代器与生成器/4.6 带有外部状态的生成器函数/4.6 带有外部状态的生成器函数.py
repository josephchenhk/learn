# -*- coding: utf-8 -*-
# @Time    : 2/3/2020 2:47 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.6 带有外部状态的生成器函数.py
# @Software: PyCharm

"""
4.6 带有外部状态的生成器函数

"""

from collections import deque

class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    # Generator 写在 iterator 里面（新用法）
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


lines = ["Python", "Java", "Python better than C++", "Java better than C++"]

linehist = Linehistory(lines)
for l in linehist:
    print(l)

print(linehist.history) # deque([(2, 'Java'), (3, 'Python better than C++'), (4, 'Java better than C++')], maxlen=3)


print("###############################################")
# 用iterator的方式：
class Linehistory2:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
        self.n = 0
        self.n_max = len(lines)

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<self.n_max:
            self.n += 1
            line = self.lines[self.n - 1]
            self.history.append((self.n, line))
            return line
        else:
            raise StopIteration

    def clear(self):
        self.history.clear()

linehist2 = Linehistory2(lines)
for l in linehist2:
    print(l)
print(linehist.history) # deque([(2, 'Java'), (3, 'Python better than C++'), (4, 'Java better than C++')], maxlen=3)