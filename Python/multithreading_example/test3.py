# -*- coding: utf-8 -*-
# @Time    : 4/12/2021 7:18 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test3.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""
from copy import copy
import time
from typing import Any, List, Callable
import threading


class Data:
    a: bool = False
    b: int = 100
    c: str = "-1"
    d: List[Any] = []

    def __str__(self):
        return f"a={self.a}, b={self.b}, c={self.c}, d={self.d}"

    __repr__ = __str__

class ModifyDataThread(threading.Thread):

    def __init__(self, name=None, callback:Callable=None):
        self.data = Data()
        threading.Thread.__init__(self, name=name)
        self.callback = callback

    def get_data(self):
        return self.data

    def run(self):
        for i in range(10):
            # Modify data
            if self.data.a:
                self.data.a = False
            else:
                self.data.a = True
            self.data.b += i
            self.data.c = str(i)
            self.data.d.append(i)
            print(f"[{threading.current_thread().name}]" + ' modify data to: ' + str(self.data))
            self.callback(self.data.a, self.data.b, self.data.c, self.data.d)
            time.sleep(1)

class UseData:

    def __init__(self):
        self.data = Data()
        print(f"\n[{threading.current_thread().name}]Initial data copy in UseData: " + str(self.data))

    def on_update(self, a, b, c, d):
        print(f"[{threading.current_thread().name}] on_update: a={a}, b={b}, c={c}, d={d}")
        self.data.a = a
        self.data.b = b
        self.data.c = c
        self.data.d = d

    def print(self):
        for i in range(10):
            print("\n")
            print(threading.current_thread().name + ' main ', i)
            print(f"[{threading.current_thread().name}] At step " + str(i) + ", data copy in UseData: " + str(self.data))
            time.sleep(1.5)


if __name__=="__main__":

    use_data = UseData()

    modify_data = ModifyDataThread(name="ModifyThread", callback=use_data.on_update)
    modify_data.start()

    use_data.print()
