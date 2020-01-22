# -*- coding: utf-8 -*-
# @Time    : 1/22/2020 7:15 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.20.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.20 合并多个字典或映射

一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类
"""

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a, b) # 在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

"""
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。 然后，这些字典并不是真的合并在一起了， ChainMap 类只是在内部创建了
一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的，比如：
"""
print(c.keys(), list(c.keys()))
print(c.values(), list(c.values()))
print(c.items(), list(c.items()))

"""
注意：对于合成字典的更新或删除操作总是影响的是列表中第一个字典。
"""
c['z'] = "I should appear in a"
print(a)
print(b)
print(dict(c))

"""
如果不用ChainMap，你也可以用update，但有两点需要注意：
（1）因为update是用后面的dict更新前面的dict，为了达到和ChainMap一样的效果，需要b.update(a); 如果a.udpate(b),则结果会和上面不一致
（2）update是会创建新的字典，之后对新字典的修改，不会改动原来合并前的字典内容
"""
c2 = dict(b)
c2.update(a)
print(c2)
print(c==c2)

c2['z'] = "I should not appear in a"
print(c2)
print(a)
