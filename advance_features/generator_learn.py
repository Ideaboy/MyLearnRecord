#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2019-1-11 10:39:13
# 杨辉三角 生成器

def triangle_yh(m):
    a = []
    b = []
    for i in range(m):
        a.append(1)
        # for j in range(i):
        #     if i >= 2 and j >= 1 and j <= i-1:
        #         a[j] = b[j-1] + b[j]
        for j in range(1, i):
            a[j] = b[j-1] + b[j]
        b = a.copy()
        yield b

if __name__ == "__main__":
    t = triangle_yh(12)
    j = 0
    SUM = 0
    inum = 0
    for i in t:
        print(i)
        j += 1
        if j == 11:
            ilist = [1] + i[:-1]
            print("ilist =", ilist)
            for x in i:
                print("inum=", inum)
                SUM += x*pow(10, inum)
                print("%d = %d*%d" %(SUM, x, pow(10, inum)))
                inum += 1
            print(SUM)
            # print(SUM//10)
            assert SUM == pow(11, j-1)
            print("SUM(%d) == pow(11, %d)" % (SUM, j-1))
