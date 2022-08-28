# -*- coding: utf-8 -*-
# @Time    : 20/3/2021 6:25 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm

from time import sleep
import threading

class BlockingDict(object):
    """
    https://stackoverflow.com/questions/26586328/blocking-dict-in-python
    """
    def __init__(self):
        self.queue = {}
        self.cv = threading.Condition()

    def put(self, key, value):
        with self.cv:
            self.queue[key] = value
            # self.cv.notify()
            self.cv.notify_all()

    def pop(self):
        with self.cv:
            while not self.queue:
                self.cv.wait()
            return self.queue.popitem()

    def get(self, key):
        with self.cv:
            while key not in self.queue:
                self.cv.wait()
            return self.queue.get(key)



blockdict = BlockingDict()

def producer():
    n = 0
    while n<5:
        print(f"put {n}")
        blockdict.put(n, f"{n}-value")
        sleep(1)
        n += 1

def consumer():
    n = 0
    while n<5:
        # v = blockdict.pop()
        v = blockdict.get(n)
        print(f"Receive {v}")
        sleep(2)
        n += 1


if __name__=="__main__":

    print("start producer")
    t = threading.Thread(target=producer, args=())
    t.start()
    # t.join()

    print("start consuming")
    consumer()

    sleep(2)
