#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019年1月7日11:44:58
# 多进程一

from multiprocessing import Process
import os


def run_process(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p1 = Process(target=run_process, args=("test",))
    print("Child process will start...")
    p1.start()
    p1.join()
    print("Child process end.")