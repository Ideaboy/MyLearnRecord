#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-27 10:54:05
# logging.basicConfig 常规使用

import logging


if __name__ == "__main__":
    data = "testdata"
    # logging.basicConfig(format="%(asctime)s")

    # logging.basicConfig(format="%(asctime)s - %(message)s")

    # logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%m/%d/%Y %I:%M%S %p")
    # 日志格式化
    logging.basicConfig(format="%(asctime)s - %(message)s")

    logging.warning("Warining! %s" % data)