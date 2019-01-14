#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019-1-7 12:00:57
# 进程池 - 批量子进程

from multiprocessing import Pool
import os, time, random
import logging


def long_time_task(name):
    logging.info("Run task %s (%s)..." % (name, os.getpid()))
    stime = time.time()
    # time.sleep(random.random() * 3)
    time.sleep(5)
    etime = time.time()
    logging.info("Task %s runs %0.2f seconds." % (name, (etime-stime)))


logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    logging.info("Parent process %s." % os.getpid())
    sztime = time.time()
    p = Pool(500)
    for i in range(1000):
        p.apply_async(long_time_task, args=(i,))
    logging.info("Waiting for all subroicesses done ...")
    p.close()
    p.join()
    logging.info("All subprocesses done.")
    edtime = time.time()
    logging.info("Parent spend time:%0.2fs" % (edtime-sztime))