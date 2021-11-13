# -- coding utf-8 --
# @Time     2021/6/27 21:22
# @Author   dicardo
# @File     local.py
# @Software PyCharm

from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '47.96.117.252',
        'NAME': 'easy_notice',
        'USER': 'root',
        'PASSWORD': 'atec@123',
        'OPTIONS': {'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'}
    }
}
