# -*- coding: utf-8 -*-
# @Time    : 6/25/2019 4:52 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 12.1.py
# @Software: PyCharm

import time
from threading import Thread

def countdown(n, thread_name):
    while n>0:
        print(f'[{thread_name}]T-minus{n}')
        n -= 1
        time.sleep(2)

def main():
    t1 = Thread(target=countdown, args=(2, "Thread_1"))
    t2 = Thread(target=countdown, args=(5, "Thread_2"))
    t1.start()
    t2.start()
    t1.join() # 等待t1执行完毕才会向下执行
    t2.join() # 等待t2执行完毕才会向下执行
    n = 6
    while n>0:
        if t1.is_alive():
            print("Thread_1 is still running")
        if t2.is_alive():
            print("Thread_2 is still running")
        if (not t1.is_alive()) and (not t2.is_alive()):
            print("Thread is completed. Waiting for main thread to terminate...")

        n -= 1
        time.sleep(2.5)
    print("Main thread completed.")

if __name__=="__main__":
    main()

