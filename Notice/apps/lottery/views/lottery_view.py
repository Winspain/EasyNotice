# -- coding utf-8 --
# @Time     2022/5/8 下午10:59
# @Author   dicardo
# @File     lottery_view.py
# @Software PyCharm

from typing import Any

from rest_framework import generics, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from common.api_rest_response import ApiRestResponse, ResponseEnum


class MyLotteryView(generics.ListCreateAPIView, viewsets.GenericViewSet):
    """
    个人lottery号码管理
    """

    def list(self, request: Request, *args: Any, **kwargs: Any) -> object:
        """
        查询个人lottery号码
        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """

        return Response(data=ApiRestResponse().response(enum=ResponseEnum.SUCCESS))

    def create(self, request: Request, *args: Any, **kwargs: Any) -> object:
        """
        新增个人lottery号码
        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        return Response(data=ApiRestResponse().response(enum=ResponseEnum.SUCCESS))
