#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-4 11:33:18
# 类的属性动态处理设计
# 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

class Chain2(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain2("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, name=''):
        name += '2018'
        return Chain2("%s/%s" % (self._path, name))

    __repr__ = __str__

if __name__ == "__main__":
    # mysql = "Mysql"
    # s = Chain().mysql.conf.int_id.setting.list.users("Tom")
    s = Chain("/gg").mysql.data
    print(s)
    s2 = Chain2().mysql.users("hello").re
    print(s2)
    print("test")

