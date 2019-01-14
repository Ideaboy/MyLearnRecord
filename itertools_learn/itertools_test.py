#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018年12月26日15:07:58
# 操作迭代对象函数

import itertools


if __name__ == "__main__":
    # 自然数迭代器
    natuals = itertools.count(1)
    # 针对上面，配置条件
    ns = itertools.takewhile(lambda x: x < 10, natuals)

    # for n in ns:
    #     if n % 2 == 0:
    #         continue
    #     print(n)
    print(next(ns))
    print(next(ns))
