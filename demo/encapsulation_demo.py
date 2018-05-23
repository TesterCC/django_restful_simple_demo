#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/2 01:59'

"""
pure python code
"""


class Request(object):

    def __init__(self, obj):
        self.obj = obj

    @property     # 方便使用，调用时不用加括号，下面让req.user 来调用
    def user(self):
        return self.obj.authticate()


class Auth(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def authticate(self):
        return True


class APIView(object):
    def dispatch(self):
        self.f2()

    def f2(self):
        a = Auth("angel", 20)
        req = Request(a)
        # print(req.obj)
        print(req.user)


if __name__ == '__main__':
    obj = APIView()
    obj.dispatch()