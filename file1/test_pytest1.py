#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-26 13:44:45

def add(a, b):
    return a+b

def test_func1():
    assert add(1, 1) == 2
    # assert add(1, 1) == 3

def test_f2():
    assert 1*2 == 2