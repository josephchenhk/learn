# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.3 让对象支持上下文管理协议.py
# @Software: PyCharm
"""
8.3 让对象支持上下文管理协议

为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法
"""


class LazyConnetion:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = None

    def __enter__(self):
        print("Enter LazyConnection")
        self.sock = "Active"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit LazyConnection")
        self.sock = "Inactive"

    def __str__(self):
        return "{} | {} | {}".format(self.address, self.port, self.sock)

    __repr__=__str__

conn = LazyConnetion("www.aqumon.com", 80)
print(conn)
with conn as c:
    print(conn)
print(conn)
