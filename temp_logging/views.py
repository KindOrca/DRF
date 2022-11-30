from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import logging
class TestLogging(APIView):
    @api_view(['GET'])
    def test_api_method(request):
        db_logger = logging.getLogger('db')

        db_logger.info('정보 메세지 !!!2@@')
        db_logger.warning('경고 !!!!!!!!!!!')

        try:
            1/0
        except Exception as e:
            db_logger.exception(e)

        return Response({'data':True}, status=HTTP_200_OK)