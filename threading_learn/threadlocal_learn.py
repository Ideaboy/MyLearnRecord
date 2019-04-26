#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019年1月7日16:21:59
# 2019年4月6日17:13:23 复习
# 作用全局而变量线程互相独立


import threading
import logging

# 全局作用变量，但变量资源独立，原理类似使用dict，以线程号为Key，获取对应对象。
local_school = threading.local()
def prost():
    std = local_school.std
    logging.info("%s , (in %s) " % (std, threading.current_thread().name))

def prot(name):
    local_school.std = name
    prost()

def prot1():
    # 这里会报错，说明 local_school.std 不存在，即上面的变量不共享
    print(local_school.std)
    prost()

class School(object):
    @property
    def sname(self):
        return self._sname

    @sname.setter
    def sname(self, name):
        self._sname = name

    @property
    def smark(self):
        return self._smark

    @smark.setter
    def smark(self, smark):
        self._smark = smark

# 该例子，对象变量还是共享
# g_name = ''
g_name = School()
g_name.smark = "M"
def ja():
    # global g_name
    logging.info("%s , %s (in %s) " % (g_name.sname, g_name.smark, threading.current_thread().name))

def yi(name, mark):
    # global g_name
    g_name.smark = mark
    g_name.sname = name + 1
    ja()

def yi1():
    # global g_name
    print(g_name.sname)
    ja()

logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    logging.info("main.")
    t1 = threading.Thread(target=prot, args=("Alice",), name="Thread-A")
    t2 = threading.Thread(target=prot, args=("Bob",), name="Thread-B")
    t0 = threading.Thread(target=prot1, args=(), name="Thread-C")
    t1.start()
    t2.start()

    t0.start()
    t0.join()
    t1.join()
    t2.join()

    t3 = threading.Thread(target=yi, args=(1, 'y'), name="Thread-J")
    t4 = threading.Thread(target=yi1, args=(), name="Thread-Y")
    import os
    logging.info(os.path.basename(__file__))

    t3.start()
    t4.start()
    t3.join()
    t4.join()