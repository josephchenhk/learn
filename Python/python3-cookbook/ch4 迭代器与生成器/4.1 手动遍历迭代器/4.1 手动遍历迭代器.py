# -*- coding: utf-8 -*-
# @Time    : 28/2/2020 3:38 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.1 手动遍历迭代器.py
# @Software: PyCharm

"""
4.1 手动遍历迭代器

"""

def manul_iter(f):
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# Generator (带yield的函数是generator)
def my_generator(data = [1, 2, 3, 5, 4]):
    for d in data:
        yield d

# Iterator (实现了__iter__ 和 __next__的类是iterator)
class my_iterator:

    def __init__(self, data = [1, 2, 3, 5, 4]):
        self.data = data
        self.n = 0
        self.n_max = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<self.n_max:
            self.n += 1
            return self.data[self.n-1]
        else:
            raise StopIteration


data = [1, 2, 3, 5, 4]
my_iterator1 = my_iterator(data)
my_iterator2 = iter(data)

print("\nTest iterator 1")
manul_iter(f=my_iterator1)
print("\nTest iterator 2")
manul_iter(f=my_iterator2)
