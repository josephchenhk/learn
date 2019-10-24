# -*- coding: utf-8 -*-
# @Time    : 10/24/2019 5:25 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 12.6.py
# @Software: PyCharm

"""
12.6 保存线程的状态信息

有时在多线程编程中，你需要只保存当前运行线程的状态。 要这么做，可使用 thread.local() 创建一个本地线程存储对象。
对这个对象的属性的保存和读取操作都只会对执行线程可见，而其他线程并不可见。
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local() # 初始化为一个 threading.local() 实例

    def __enter__(self):
        # 错误的示范，因为不同线程会对self.sock竞争
        # self.sock = socket(self.family, self.type)
        # self.sock.connect(self.address)

        # 正确，通过self.local来保证线程安全
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        # 错误的示范，因为不同线程会对self.sock竞争
        # self.sock.close()

        # 正确，通过self.local来保证线程安全
        self.local.sock.close()
        del self.local.sock

# 测试

from functools import partial
def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')

        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))

    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()