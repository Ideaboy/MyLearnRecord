#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019年1月7日16:21:59
# 作用全局而变量线程互相独立


import threading
import logging

local_school = threading.local()

def prost():
    std = local_school.std
    logging.info("%s (in %s) " % (std, threading.current_thread().name))

def prot(name):
    local_school.std = name
    prost()

class School(object):
    @property
    def sname(self):
        return self._sname

    @sname.setter
    def sname(self, name):
        self._sname = name


# g_name = ''
g_name = School()
def ja():
    # global g_name
    logging.info("%s (in %s) " % (g_name.sname, threading.current_thread().name))

def yi(name):
    # global g_name
    g_name.sname = name + 1
    ja()

logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    logging.info("main.")
    t1 = threading.Thread(target=prot, args=("Alice",), name="Thread-A")
    t2 = threading.Thread(target=prot, args=("Bob",), name="Thread-B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    t3 = threading.Thread(target=yi, args=(1,), name="Thread-J")
    t4 = threading.Thread(target=yi, args=(9,), name="Thread-Y")

    t3.start()
    t4.start()
    t3.join()
    t4.join()