#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019-1-7 17:34:17
# 分布式进程

import random
import time
import queue
from multiprocessing.managers import BaseManager

'''
实现方法(master)：
1、创建Queue队列
2、Queue注册，回调关联
3、绑定端口和设置验证
4、启动
5、通过网络访问Queue对象
6、执行任务.....
...tesk.put(n)
...result.get(timeout=10)
-1、关闭
'''
# 1
task_queue = queue.Queue()
result_queue = queue.Queue()

# 2
class QueueManager(BaseManager):
    pass

# windows下 无法pickling
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

if __name__ == "__main__":
    # 3
    QueueManager.register("get_task_queue", callable=return_task_queue)
    QueueManager.register("get_result_queue", callable=return_result_queue)

    # 4
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b'abc')

    # 5
    manager.start()

    # 6
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 执行任务
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d..." % n)
        task.put(n)

    print("Try get results..")

    for i in range(10):
        r = result.get(timeout=10)
        print("Result: %s" % r)

    # -1
    manager.shutdown()
    print("master exit.")



