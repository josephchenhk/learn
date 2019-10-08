from itertools import chain

a = [1, 2, 3, 4]
b = ('x', 'y', 'z')
# 不要求a和b类型一致，只要是迭代器都可以
for x in chain(a,b):
    print(x)