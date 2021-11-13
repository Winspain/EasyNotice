# -- coding utf-8 --
# @Time     2021/7/3 14:32
# @Author   dicardo
# @File     api_logging_middleware.py
# @Software PyCharm

from __future__ import unicode_literals
import logging
import time


class ApiLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_logger = logging.getLogger('api')

    def __call__(self, request):
        request.start_time = time.time()
        body = str(request.body) + str(request.POST)
        response = self.get_response(request)
        execute_time = round((time.time() - request.start_time) * 1000)

        if request.method != 'GET':
            self.api_logger.info(f'{request.user} {execute_time}ms {request.method} {request.path} {body} {response.status_code} {response.reason_phrase}')

        else:
            self.api_logger.info(f'{request.user} {execute_time}ms {request.method} {request.path} {response.status_code} {response.reason_phrase}')
        return response
