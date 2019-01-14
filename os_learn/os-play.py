#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-25 14:21:42
# os 操作实践 1  路径目录操作

import os
import time

if __name__ == "__main__":
    #为什么加的 {.} ？
    print(os.path.abspath('.'))
    abspath = os.path.abspath('.')

    # 与直接拼接对比，该方法适用于各种系统（可移植性)
    # （最后路径的）拆分：os.path.split 目录 、os.path.splitext() 文件扩展名
    newpath = os.path.join(abspath, 'OsPathJoin_test')
    print(newpath)

    # 创建目录
    # os.mkdir(newpath)
    # 延时下
    # time.sleep(3)
    # 删除目录
    # os.rmdir(newpath)

    # os.rename(newpath, 'NewFileName')
    # os.rename('NewFileName', 'NewFileName.txt')
    # 拒绝访问。
    # os.remove('onlyname')

    filename1 = os.path.abspath(__file__)
    fname2 = os.path.dirname(filename1)
    fname3 = os.path.dirname(fname2)
    print("os.path.abspath(__file__):", filename1)
    print("os.path.dirname(filename):", fname2)
    print("os.path.dirname(filename):", fname3)

    fpath = os.path.abspath('.')
    ffpath = os.path.abspath('..')
    print("fpath", fpath)
    print("ffpath:", ffpath)
