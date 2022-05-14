# -- coding utf-8 --
# @Time     2022/5/14 下午10:16
# @Author   dicardo
# @File     lottery_serializer.py
# @Software PyCharm

from rest_framework import serializers

from lottery.models import MyLotteryInfo


class LotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLotteryInfo
        fields = '__all__'
