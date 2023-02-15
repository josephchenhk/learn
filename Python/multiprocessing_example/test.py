# -*- coding: utf-8 -*-
# @Time    : 5/2/2021 2:43 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: pair_trading.py
# @Software: PyCharm

from functools import wraps
from time import sleep
from multiprocessing import Pool, Process, Manager
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
    sleep(1)
    print(f"func({x})=2*{x} executed.")
    res = 2 * x
    if ret_list is not None:
        ret_list.append(res)
    return res


class Test:
    """"""

    X = list(range(20000))
    manager = Manager()

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
        p = Pool(4)
        results = []
        for x in self.X:
            results.append(p.apply_async(func, (x,)))
        p.close()
        p.join()

        print([r.get() for r in results])

    @timeit
    def parallel1(self, func):
        p = Pool(4)
        results = p.map_async(func, self.X)
        p.close()
        p.join()
        print(results.get())


    @timeit
    def parallel2(self, func):
        return_list = self.manager.list()  # 可以使用列表list
        # return_dict = self.manager.dict() # 也可以使用列表dict
        i = 0
        while i < len(self.X):
            X = self.X[i:i + 4]
            jobs = []
            for x in X:
                p = Process(target=func, args=(x, return_list))
                jobs.append(p)
                p.start()

            for proc in jobs:
                proc.join()
            i += 4
        print(return_list)


if __name__ == "__main__":
    test = Test()

    print("double:")
    test.sequential(double)
    print("-----------------------\n")
    test.parallel1(double)

    print("=======================\n")

    print("double_with_sleep:")
    test.setX(range(4))
    test.sequential(double_with_sleep)
    print("-----------------------\n")
    test.parallel1(double_with_sleep)

    """
    double:
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
    sequential Elapsed time: 4.853199999999003e-05 seconds
    -----------------------

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
    parallel Elapsed time: 0.116941709 seconds
    =======================

    double_with_sleep:
    func(0)=2*0 executed.
    func(1)=2*1 executed.
    func(2)=2*2 executed.
    func(3)=2*3 executed.
    [0, 2, 4, 6]
    sequential Elapsed time: 4.013663917 seconds
    -----------------------

    func(0)=2*0 executed.
    func(1)=2*1 executed.func(2)=2*2 executed.

    func(3)=2*3 executed.
    [0, 2, 4, 6]
    parallel Elapsed time: 1.049143343 seconds
    """
