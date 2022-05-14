from django.db import models


# Create your models here.

class LotteryInfo(models.Model):
    drawNum = models.CharField(unique=True, max_length=50, verbose_name='开奖期号')
    drawResult = models.CharField(max_length=100, verbose_name='开奖结果')
    drawTime = models.DateField(verbose_name='开奖日期')
    state = models.CharField(max_length=100)
    isDeleted = models.BooleanField()
    createdBy = models.CharField(max_length=100)
    updateBy = models.CharField(max_length=100)
    createdTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'lottery_info'


class MyLotteryInfo(models.Model):
    selectNum = models.CharField(max_length=100, verbose_name='开奖结果')
    state = models.CharField(max_length=100)
    isDeleted = models.BooleanField()
    createdBy = models.CharField(max_length=100)
    updateBy = models.CharField(max_length=100)
    createdTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(null=True)

    class Meta:
        db_table = 'lottery_select'
