#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019-1-4 17:47:00
# 线程类的继承测试

import threading
import time
import logging

class Mythreading(threading.Thread):
    def __init__(self, thname, t, mydaemon=False):
        threading.Thread.__init__(self, daemon=mydaemon)
        self._thname = thname
        self._t = t

    def run(self):
        logging.info(self._thname + " threading start, will spend %s s" % self._t)
        time.sleep(self._t)
        logging.info(self._thname + " threading end.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(logging.INFO) # 在多线程中，该方法不稳定
    stime = time.time()
    logging.info("Main start...")

    t1 = Mythreading("t1", 3)
    t2 = Mythreading("t2", 4, mydaemon=True)
    t1.start()
    t2.start()
    # .join() 方式：堵塞     作用：线程同步
    # t1.join() #可抵消daemon=True
    # t2.join()
    time.sleep(1)
    etime = time.time()
    logging.info("Main end. \nSpend time: %ss" % (etime-stime))