# -*- coding: utf-8 -*-
# @Time    : 3/3/2020 3:37 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 4.7 迭代器切片.py
# @Software: PyCharm

"""
4.7 迭代器切片

迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。 函数 islice() 返回一个可以生成指定元素的迭代器，它通过
遍历并丢弃直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置。
"""

def count(n):
    while n<25:
        yield n
        n += 1

c = count(0)
try:
    print(c[10:20])
except TypeError as e:
    print(e)

# use itertools.isslice()
import itertools
c = count(0)
try:
    print(list(itertools.islice(c,10,20))) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
except Exception as e:
    print(e)

"""
这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实。 所以如果你需要之后再次访问这个迭代器的话，
那你就得先将它里面的数据放入一个列表中。

20
21
22
23
24
"""
for n in c: # 这里的c已经被消耗0-19，所以print会从20开始
    print(n)
