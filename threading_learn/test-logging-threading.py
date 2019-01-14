#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 进程熟悉 logging使用

# 2018-12-24 17:51:16

import threading
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def func(string, st):
    logger.info(string + " in threading~，will spend %s s" %st)
    time.sleep(st)
    logger.info(string + " out threading!")


if __name__ == "__main__":
    print("这是主线程开始标志")
    func("t0", 2)
    t1 = threading.Thread(target=func, args=('t1', 2), daemon=False)
    # 守护进程，若该线程是最后结束，怎么在此之前结束。
    # 若该线程不是最后运行结束，怎么守护进程等于“无”
    t2 = threading.Thread(target=func, args=("t2", 3), daemon=True)

    t1.start()
    t2.start()
    time.sleep(2)
    print("主线程结束标志!")


