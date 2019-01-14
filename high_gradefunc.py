#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-11-13 09:25:18



def func(x):
    return x*2

# map
def standard_Eg(x):
    return x.capitalize()

def func1(x):
    return x

# filter
def huishu(num):
    m = bool
    snum = str(num)
    le = len(str(num))
    print(le)
    if le % 2 == 1:
        n = (le - 1) // 2
    else:
        n = le // 2
    for i in range(n):
        if snum[i] == snum[-(i+1)]:
            m = True
            continue
        else:
            m = False
            break
    if m:
        print("是回数")
    else:
        print("不是回数")

    # return "是回数"

# sorted

# lambda
def lmdFunction():
    return lambda x: x+2


if __name__ == "__main__":
    print(type(map(func, [1, 2, 3])))
    print(map(func, [1, 2, 3]))
    string = ["ToM", "jaCK", "KAKA"]
    print(list(map(standard_Eg, string)))

    '''使用 sorted 回数检测实现'''
    huishu(123000021)

    # sorted
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    std = sorted(L, key=lambda x: x[1], reverse=True)
    print(std)

    # lambda
    x = 2
    lmd = lambda: x+1
    lsum = lmdFunction()
    # 这说明，函数包装返回的lambda 调取不了外部变量，
    # 而直接赋予lambda对象的，可以使用
    print(lmd(), lsum, lsum(8))

