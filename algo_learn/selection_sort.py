#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019-5-4 11:43:13
# 选择排序
"""
从未排序区域，选取一个元素，然后从左到右，依次比较，
较小的与之交换位置，遍历一遍。
再从未排序区域，选取一元素，上同。
上面取小指，也可去大指，类同。
时间复杂度都是O（n^2)
唯一优点，不占用额外内存
"""
def selection_sort(dlist):
    lenlist = len(dlist)
    for i in range(lenlist):
        for j in range(i+1, lenlist):
            if dlist[i] > dlist[j]:
                dlist[i], dlist[j] = dlist[j], dlist[i]
    return dlist

if __name__ == "__main__":
    slit = [100, 20, 33, 50, 99, 1, -20]
    selist = selection_sort(slit)
    print(selist)