#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019年1月7日18:25:46
# 分布 - 工人

import time
import sys
import queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

server_addr = "127.0.0.1"
print("Connect to server %s" % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d..." % (n, n))
        r = "%d * %d = %d" % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task queue is empty.")

print("worker exit.")

# if __name__ == "__main__":
#     pass