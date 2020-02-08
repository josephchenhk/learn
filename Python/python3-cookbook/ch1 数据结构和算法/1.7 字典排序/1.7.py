# -*- coding: utf-8 -*-
# @Time    : 1/17/2020 3:19 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.7.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.7 字典排序

python里普通的字典是不带顺序的，如果想保持插入的顺序的话，可以用collections模块中的OrderDict类.
但需要注意OrderDict的缺点：它是普通字典的两倍大小，因为其内部维护者另一个链表以记录元素的插入顺序。
"""
import json

normal_dict = {}
normal_dict['foo'] = 2
normal_dict['bar'] = 1
normal_dict['spam'] = 4
normal_dict['grok'] = 3
for key in normal_dict:
    print(key, normal_dict[key])
print(normal_dict)  # >> {'foo': 2, 'bar': 1, 'spam': 4, 'grok': 3}
normal_dict_dump = json.dumps(normal_dict)
print(normal_dict_dump)  # >> {"foo": 2, "bar": 1, "spam": 4, "grok": 3} ?? 似乎普通的dict也能维护插入顺序?

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['foo'] = 2
ordered_dict['bar'] = 1
ordered_dict['spam'] = 4
ordered_dict['grok'] = 3
for key in ordered_dict:
    print(key, ordered_dict[key])
print(ordered_dict)  # >> OrderedDict([('foo', 2), ('bar', 1), ('spam', 4), ('grok', 3)])

"""OrderedDict被json序列化之后，仍然可以保持顺序"""
ordered_dict_dump = json.dumps(ordered_dict)
print(ordered_dict_dump)  # >> {"foo": 2, "bar": 1, "spam": 4, "grok": 3}
