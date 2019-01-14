#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 装饰器 速览
import time
import functools

# 通用的装饰器
def log(func):
    def wrapper(*args, **kw):
        print(time.time(), func.__name__)
        return func(*args, **kw)
    return wrapper

# 有参数的装饰器 实现方法 再加一层函数
# 具有 调用 __name__ 与预期不同 缺陷
def LOG(*text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s, %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 完备的装饰器实现
def Log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(time.time(), func.__name__)
        return func(*args, **kw)
    return wrapper


def func1():
    print("func1")

@log
def func2():
    print("func2")

@log
def func3(x):
    print("x:", x)


@LOG("Hello", "Hi")
def func4():
    print("This is func4")

@Log
def func5():
    print("Log装饰")

if __name__ == "__main__":
    func1()
    func2()
    func3(3)
    func4()
    func5()
    # 被装饰过的函数，__name__ 指向变化成 wrapper
    print(func2.__name__)

    print(func5.__name__)