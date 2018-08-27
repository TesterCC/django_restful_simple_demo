# coding=utf-8
import json

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View


# Create your views here.


def users(request):
    user_list = ["TesterCC", "MFC", "YMSZ"]
    return HttpResponse(json.dumps(user_list))


# 继承（多个类共用的功能，为了避免重复重复编写）
class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        print(">>>{}".format(request))
        print("before")
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print("after")
        return ret


# 多继承优先级从左到右
class StudentsView(MyBaseView, View):

    def get(self, request, *args, **kwargs):
        print("This is GET method.")
        return HttpResponse("GET")

    # head method will response directly, not enter this view

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST")

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def patch(self, request, *args, **kwargs):
        return HttpResponse("PATCH")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("DELETE")

    def trace(self, request, *args, **kwargs):
        return HttpResponse("TRACE")

    def options(self, request, *args, **kwargs):
        return HttpResponse("OPTIONS")


class Teacher(MyBaseView, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("GET")

    # head method will response directly, not enter this view

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST")

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def patch(self, request, *args, **kwargs):
        return HttpResponse("PATCH")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("DELETE")

    def trace(self, request, *args, **kwargs):
        return HttpResponse("TRACE")

    def options(self, request, *args, **kwargs):
        return HttpResponse("OPTIONS")
