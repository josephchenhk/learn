#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))            # connect 以后连接成功
    for i in range(10):
        s.sendall(b'Hello, world')
        data = s.recv(1024)            # recv是block函数，直到接收到数据以后才会运行（收到server传回的信息以后才会继续运行）
        print('Received', repr(data),i)