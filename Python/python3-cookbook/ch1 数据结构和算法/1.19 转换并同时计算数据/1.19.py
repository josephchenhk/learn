# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 7:07 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.19.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.19 转换并同时计算数据

一个优雅的方法是使用生成器表达式：
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

"""
这里注意两点：
1. 你并不需要多加一对括号 (): sum((x * x for x in nums)) 实际上等价于 sum(x * x for x in nums)
2. 用列表表达式也可以得到同样的结果，但通常消耗更多内存，不如生成器表达式好：sum([x * x for x in nums]) is OK but not GOOD.
"""