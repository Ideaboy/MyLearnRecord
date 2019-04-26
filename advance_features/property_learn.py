#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-12-3 18:15:27

# 类的方法 转换成 “属性”方式调用

class BaseClass(object):
    def score(self):
        return self._score

    def set_score(self, value):
        self._score = value
        return self._score

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == "__main__":
    # s = BaseClass()
    # print(s.score())

    st = Student()
    st.score = 66
    print(st.score)
