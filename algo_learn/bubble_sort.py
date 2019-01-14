#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019年1月7日09:52:13
# 回顾冒泡排序


def bubble_sort(bslist):
    rlist = []
    for i in range(len(bslist)):
        for j in range(len(bslist)-i-1):
            if bslist[j] > bslist[j+1]:
                bslist[j+1], bslist[j] = bslist[j], bslist[j+1]
    return bslist


if __name__ == "__main__":
    slit = [100, 20, 33, 50, 99, 1, -20]
    rl = bubble_sort(slit)
    print(rl)
