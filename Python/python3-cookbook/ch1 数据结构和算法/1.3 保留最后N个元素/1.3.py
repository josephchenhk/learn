# -*- coding: utf-8 -*-
# @Time    : 1/15/2020 3:24 PM
# @Author  : Joseph Chen
# @Email   : info@atabet.com
# @FileName: 1.3.py
# @Software: learn
# Copyright 2020 Atabet Limited

"""
1.3 保留最后N个元素

保留有限历史记录正是 collections.deque
"""
import io
from collections import deque

def search(lines, pattern, history=2):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__=="__main__":

    # Simulate a file
    sim_file = io.StringIO()
    sim_file.write("first line.\n")
    sim_file.write("second line with python.\n")
    sim_file.write("third line with java.\n")
    sim_file.write("fourth line with python.\n")
    sim_file.write("fifth line is end.\n")

    # reset the buffer position to the beginning
    sim_file.seek(0)

    # print output:
    # 0 first line.
    #
    # 1 second line with python.
    #
    # 2 third line with java.
    #
    # 3 fourth line with python.
    #
    # 4 fifth line is end.

    for n, line in enumerate(sim_file.readlines()):
        print(n, line)

    # reset the buffer position to the beginning
    sim_file.seek(0)

    for line, prevlines in search(sim_file.readlines(), "python", 2):
        for pline in prevlines:
            print("previous lines: ", pline, end='')
        print("pattern match line: "line, end='')
        print('-' * 20)
