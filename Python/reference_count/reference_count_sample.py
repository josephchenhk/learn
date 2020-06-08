# -*- coding: utf-8 -*-
# @Time    : 8/6/2020 7:29 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: reference_count_sample.py
# @Software: PyCharm

import sys

def test_refcount(a):
    print("func a refcount: {}".format(sys.getrefcount(a)))

if __name__ == '__main__':

    # 直接创建Python对象
    a = 189987319
    print("a refcount: {}".format(sys.getrefcount(a)))

    # 调用一次Python对象a，则引用计数器加1
    b = a
    print("b, a refcount: {}".format(sys.getrefcount(a)))

    # 存入列表，字段，或者元组中，引用计数器都会加1
    c = [a]
    print("c, a refcount: {}".format(sys.getrefcount(a)))

    # 使用函数调用的时候，传参的时候引用计数器加1，调用的时候引用计数器也会加1，因此是加2
    test_refcount(a)

    """
    ???
    a refcount: 3
    b, a refcount: 4
    c, a refcount: 5
    func a refcount: 8
    """