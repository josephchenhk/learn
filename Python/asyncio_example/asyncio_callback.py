# -*- coding: utf-8 -*-
# @Time    : 9/10/2019 9:44 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: asyncio_callback.py
# @Software: PyCharm

import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(coroutine)

# # 方法一：调用callback处理结果
# future.add_done_callback(callback)
# loop.run_until_complete(future)

# 方法二：直接通过future.result()取出结果
loop.run_until_complete(future)
print(f"Future returns: {future.result()}")

print('TIME: ', now() - start)