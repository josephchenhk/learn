# -*- coding: utf-8 -*-
# @Time    : 4/3/2021 10:23 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm

from functools import wraps
from time import sleep
from threading import Thread
from multiprocessing.pool import ThreadPool
from timeit import default_timer as timer


def timeit(func):
    """Measure execution time of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        tic = timer()
        res = func(*args, **kwargs)
        toc = timer()
        print("{} Elapsed time: {} seconds".format(func.__name__, toc - tic))
        return res

    return wrapper


def double(x: int, ret_list: list = None) -> int:
    res = 2 * x
    if ret_list is not None:
        ret_list.append(res)
    return res


def double_with_sleep(x: int, ret_list: list = None) -> int:
    sleep(0.1)
    print(f"func({x})=2*{x} executed.")
    res = 2 * x
    if ret_list is not None:
        ret_list.append(res)
    return res


class Test:
    """"""

    X = list(range(40))

    def setX(self, X):
        self.X = X

    @timeit
    def sequential(self, func):
        results = []
        for x in self.X:
            results.append(func(x))
        print(results)

    @timeit
    def parallel(self, func):

        results = []
        threads = []
        for x in self.X:
            t = Thread(target=func, args=(x, results), daemon=True)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


        print(results)

    @timeit
    def parallel2(self, func):
        p = ThreadPool(10)
        results = []
        for x in self.X:
            results.append(p.apply_async(func, (x,)))
        p.close()
        p.join()
        print([r.get() for r in results])

    @timeit
    def parallel3(self, func):
        p = ThreadPool(10)
        results = p.map_async(func, self.X)
        p.close()
        p.join()
        print(results.get())



if __name__ == "__main__":
    test = Test()
    #
    # print("double:")
    # test.sequential(double)
    # print("-----------------------\n")
    # test.parallel(double)

    print("=======================\n")

    print("double_with_sleep:")
    test.sequential(double_with_sleep)
    print("-----------------------\n")
    test.parallel2(double_with_sleep)