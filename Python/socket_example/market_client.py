#!/usr/bin/env python3

import socket

HOST = '192.168.9.83'  # The server's hostname or IP address
PORT = 5566        # The port used by the server
end = '\n'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))            # connect 以后连接成功

    s.sendall(b'CN_60_MA1909\n')
    s.sendall(b'CN_60_a1909\n')
    n = 0
    data = ''
    print("Connected.")
    while True:
        streamBytes = s.recv(1024)  # recv是block函数，直到接收到数据以后才会运行（收到server传回的信息以后才会继续运行）
        data += streamBytes.decode()
        if '\n' in streamBytes.decode():
            print(n, repr(data))
            data = ''
            n += 1