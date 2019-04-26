#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019-3-31 21:46:052
# tcp 协议演练
# 对象：服务端

import socket
import threading
import time

def tcplink(sock, addr):
    print("Accept new connetion form %s:%s..." % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        # bdata = bytes(data.encode('utf-8'))
        time.sleep(1)
        if not data and data.decode('utf-8') == "exit":
            break
        # sock.send(b"Hello, %s!" % data.decode('utf-8')).encode('utf-8')  无法发送
        # .send() 形参类型要求为 bytes
        sock.send(b"Hello," + data.decode('utf-8').encode('utf-8') + b"!")
    sock.close()
    print("Connection form %s:%s closed." % addr)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听端口
    s.bind(("127.0.0.1", 8848))

    s.listen(1)
    print("Waiting for connection...")

    while True:
        # 接收一个新链接
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


