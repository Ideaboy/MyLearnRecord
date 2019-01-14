#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018年12月27日10:17:06
# logging 等级规则

import logging



if __name__ == "__main__":
    """
    NOTSET  0
    DEBUG   10
    INFO    20
    WARNING 30
    ERROR   40
    CRITICAL    50
    """
    """默认logging 等级为 warning 30 小于这个等级值的，都不会发日志"""

    # 日志写入.log文档    level 等级过滤
    # logging.basicConfig(filename='test.log', filemode='w', level=logging.ERROR)
    logging.basicConfig(level=logging.INFO)

    logging.debug("This is debug ,level = 10")
    logging.info("Hello INFO")
    logging.warning("Warning 30")
    logging.error("Error 40")
    logging.critical("critical 50")

    logging.info("Info too")
    logging.debug("This is debug")

    print('admin/')