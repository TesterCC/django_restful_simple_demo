# coding=utf-8

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView

from api.models import UserInfo, UserToken


def md5(user):
    import hashlib
    import time

    ctime = str(time.time())

    # 字符串变字节
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding="utf-8"))

    return m.hexdigest()


class AuthView(APIView):

    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}

        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')

            obj = UserInfo.objects.filter(user_name=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'

            # 为登陆用户创建Token
            token = md5(user)

            # 存在就更新，不存在就创建
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})

            ret['token'] = token

        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)  # 避免自己来处理返回Json格式数据
