import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()   # accept是block函数，直到client运行connect以后才会运行
    with conn:                # conn是新建立的socket连接，该连接表示与客户端相连的连接
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)     # recv是block函数，直到接收到数据以后才会运行
            print(data)
            if not data:
                break
            conn.sendall(data)
