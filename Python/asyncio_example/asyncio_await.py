# -*- coding: utf-8 -*-
# @Time    : 9/10/2019 10:22 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: asyncio_await.py
# @Software: PyCharm

"""
阻塞和await
使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。协程遇到await，
事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行。

耗时的操作一般是一些IO操作，例如网络请求，文件读取等。我们使用asyncio.sleep函数来模拟IO操作。协程的目的也是让这些IO操作
异步化。
"""
import asyncio
import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(3)

futures = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

loop = asyncio.get_event_loop()
# print(loop.run_until_complete(asyncio.wait(futures)))
print(loop.run_until_complete(asyncio.gather(*futures)))   # ['Done after 1s', 'Done after 2s', 'Done after 3s']

for future in futures:
    print('Task ret: ', future.result())

print('TIME: ', now() - start)