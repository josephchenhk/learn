"""
heapq.merge() 需要所有输入序列必须是排过序的。 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做
任何的排序检测。 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。
"""

import heapq

a = [1, 4, 8, 10]
b = [2, 3, 7, 9]

print(list(heapq.merge(a,b)))