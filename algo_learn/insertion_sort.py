#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019年5月4日14:40:11
# 插入排序
"""
    第一个元素设为有序区，选取后面元素，向前遍历比较，
    最小的插入在比较元素前。
    较大的直接赋值后移，一直比较，直至最小，在上个位置插入赋值即可。
"""
def insertion_sort(dlist):
    for i in range(0, len(dlist)):
        preindex = i-1
        current = dlist[i]
        while preindex >= 0 and dlist[preindex] > current:
            dlist[preindex+1] = dlist[preindex]
            preindex -= 1
        dlist[preindex+1] = current
    return dlist



if __name__ == "__main__":
    slit = [100, 20, 55, 50, 99, 1, -20]
    rl = insertion_sort(slit)
    print(rl)
