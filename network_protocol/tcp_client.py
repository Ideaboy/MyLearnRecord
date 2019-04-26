#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019年3月31日22:16:51
# TCP
# 客户端

import socket


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(("127.0.0.1", 8848))
    # 接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in [b'mc', b'ty', b'sh']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()