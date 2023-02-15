# -*- coding: utf-8 -*-
# @Time    : 4/12/2021 7:18 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test2.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""
import time
from typing import Any, List
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

    def __init__(self, name=None):
        self.data = Data()
        threading.Thread.__init__(self, name=name)

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
            print(threading.current_thread().name + ' modify data to: ' + str(self.data))
            time.sleep(1)

class UseData:

    def __init__(self):
        self.modify_data = ModifyDataThread(name="ModifyThread")
        self.modify_data.start()
        self.data = self.modify_data.get_data()
        print("Initial data in UseData: " + str(self.data))

    def wait_and_print(self):
        for i in range(10):
            print("\n")
            print(threading.current_thread().name + ' main ', i)
            print("At step " + str(i) + ", data in UseData: " + str(self.data))
            time.sleep(1.5)

if __name__=="__main__":
    # modify_data = ModifyDataThread(name="ModifyThread")
    # modify_data.start()
    #
    # for i in range(10):
    #     print("\n")
    #     print(threading.current_thread().name + ' main ', i)
    #     if modify_data.is_alive():
    #         print(modify_data.get_data())
    #     else:
    #         print(modify_data.name + ' is dead.')
    #     time.sleep(1.5)

    use_data = UseData()
    use_data.wait_and_print()
