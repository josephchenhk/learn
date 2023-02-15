# -*- coding: utf-8 -*-
# @Time    : 10/24/2019 5:32 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 12.7.py
# @Software: PyCharm

"""
12.7 创建一个线程池

你创建一个工作者线程池，用来响应客户端请求或执行其他的工作。
concurrent.futures 函数库有一个 ThreadPoolExecutor 类可以被用来完成这个任务。 下面是一个简单的TCP服务器，使用了一个
线程池来响应客户端：
"""

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()

def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

echo_server(('',15000))
