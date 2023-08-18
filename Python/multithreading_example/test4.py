# -*- coding: utf-8 -*-
# @Time    : 18/8/2023 10:40 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test4.py

"""
Copyright (C) 2022 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the terms of the JXW license,
which unfortunately won't be written for another century.

You should have received a copy of the JXW license with this file. If not,
please write to: josephchenhk@gmail.com
"""
import time
import threading
from multiprocessing.pool import ThreadPool
from functools import partial

# Create a lock
lock = threading.Lock()

class SharedClass:

    # Shared variable
    shared_variable = 0

    def update(self, num: int):
        with lock:
            time.sleep(0.5)
            self.shared_variable += num
            print(self.shared_variable)



# Function to modify the shared variable
def modify_shared_variable(shared_class: SharedClass, num: int):
    shared_class.update(num)


shared_class = SharedClass()

p = ThreadPool(2)
result = []
for num in (4, 5):
    res = p.apply_async(
        modify_shared_variable,
        (shared_class,
         num)
    )
    result.append(res)
p.close()
p.join()
final_result = [r.get() for r in result]
print(shared_class.shared_variable)

# Create two threads
thread1 = threading.Thread(
    target=modify_shared_variable,
    args=(shared_class, 4,)
)
thread2 = threading.Thread(
    target=modify_shared_variable,
    args=(shared_class, 5,)
)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final value of the shared variable
print(shared_class.shared_variable)
