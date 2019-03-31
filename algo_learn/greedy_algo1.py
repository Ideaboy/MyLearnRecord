#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019-1-13 11:22:04
# 贪心算法，一定时间内公共场所安排最多场活动

def takeSecond(elem):
    return elem[1]

# 字典排序，根据v中的值
def dict_sort(dicts):
    a = []
    rdict = {}
    for v in dicts.values():
        a.append(v)
    a.sort(key=takeSecond)
    print(a)

    # 排序后的字典
    for i in a:
        for k in dicts.keys():
            if dicts[k] == i:
                rdict[k] = i
    return rdict

# 贪心算法 - 活动安排
class greedy_selector(object):
    def __init__(self, d):
        self._d = d
        self._k = []
        self._v = list(d.values())
        self._actlist = [0]

    def select(self):
        j = 1
        count = 1
        actlist = []
        # for k, v in self._d.items():
        #     self._k.append(k)
        #     self._v.append(v)

        for i in range(1, len(self._d)):
            if self._v[i][0] > self._v[j][1]:
                # print("i:", i, "j:", j)
                # print(self._v[i][0], ">", self._v[j][1])
                j = i
                count += 1
                self._actlist.append(i)
        print("选择序列", self._actlist)
        # return count
        return self._actlist

    def greedy_select(self):
        j = 0
        alist = [0]
        for i in range(1, len(self._d)):
            if self._v[j][1] < self._v[i][0]:
                # print("front_end:", i, "atonce_start:", j)
                # print(self._v[i][0], ">", self._v[j][1])
                j = i
                alist.append(i)
                continue
        return alist

    def get_actlist(self, actlist):
        rlist = []
        for i in actlist:
            rlist.append(list(self._d.values())[i])
        return rlist

if __name__ == "__main__":
    actvitiylist = {
        "丁": (5, 7),
        "甲": (1, 4),
        "甲2": (12, 14),
        "己": (5, 9),
        "壬": (8, 12),
        "乙": (3, 5),
        "丙": (0, 6),
        "戊": (3, 8),
        "庚": (6, 10),
        "辛": (8, 11),
        "癸": (2, 13)
    }
    print(type(actvitiylist))
    rd = dict_sort(actvitiylist)
    print(rd)


    g = greedy_selector(rd)
    slit1 = g.select()
    print("len(slit1)=", len(slit1))
    actlist = g.get_actlist(slit1)
    print("g.select -> ", actlist)

    slit2 = g.greedy_select()
    print(slit2)
    print(g.get_actlist(slit2))