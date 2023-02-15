# -*- coding: utf-8 -*-
# @Time    : 7/4/2021 3:25 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: random_walk.py
# @Software: PyCharm

"""
Random Walk (Implementation in Python)

Ref: https://www.geeksforgeeks.org/random-walk-implementation-python/
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def gen_random_walk(start:int=2, N:int=1000):
    assert N>1, f"A random walk at least includes two elements, but N={N} is given."
    # Probability to move up or down (90% probability it stays unchanged)
    prob = [0.05, 0.95]

    # statically defining the starting position
    positions = [start]

    # creating the random points
    rr = np.random.random(N-1)
    downp = rr < prob[0]
    upp = rr > prob[1]

    for idownp, iupp in zip(downp, upp):
        down = idownp and positions[-1] > 1
        up = iupp and positions[-1] < 4
        positions.append(positions[-1] - down + up)

    return positions

if __name__=="__main__":
    # plotting down the graph of the random walk in 1D
    positions = gen_random_walk(1000)
    plt.plot(positions)
    plt.show()
