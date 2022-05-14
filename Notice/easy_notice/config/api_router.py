# -- coding utf-8 --
# @Time     2021/6/27 21:40
# @Author   dicardo
# @File     api_router.py
# @Software PyCharm

"""drf路由"""

from rest_framework.routers import DefaultRouter

from apps.users.views.example_views import ExampleView
from lottery.views.lottery_view import MyLotteryView

router = DefaultRouter()
urlpatterns = router.urls
router.register('example/v1/celery', ExampleView, basename='ExampleView')
# router.register('easyNotice/v1/myLottery', MyLotteryView, basename='MyLotteryView')
