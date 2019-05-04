#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-25 15:01:29
# 常用内建函数 datetime

# from 模块名
from datetime import datetime


if __name__ == "__main__":
    nowtime = datetime.now()
    print(nowtime)  # 2018-12-25 15:02:50.252130

    dt1 = datetime(2018, 12, 25, 15)
    print(dt1)  # 2018-12-25 15:00:00




