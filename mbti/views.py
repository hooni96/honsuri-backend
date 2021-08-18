import json

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets # vieset import
from .serializers import MbtiSerializer # 생성한 serializer import
from mbti.models import Mbti # 선언한 모델 import

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.schemas.openapi import AutoSchema

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
      
from django.shortcuts import get_object_or_404

class MbtiView(generics.RetrieveAPIView): 
    '''
    mbti 질문과 보기를 반환하는 api
    ---
    '''
    queryset = Mbti.objects.all() 
    serializer_class = MbtiSerializer 

# class MbtiViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
#     queryset = Mbti.objects.all() # 존재하는 테이블의 데이터를 전부 가져오겠다는 뜻
#     serializer_class = MbtiSerializer # 이전에 생성하였던 MbtiSerializer 클래스를 이용하겠다는 뜻

# class MbtiView(generics.ListAPIView): 
#     '''
#     mbti 질문과 보기를 반환하는 api
#     ---
#     parameter: mbtiId
#     return: question, answer
#     '''
#     # manual parameter
#     mbtiId = openapi.Parameter(
#         'mbtiId', 
#         openapi.IN_QUERY, 
#         description='페이지 번호', 
#         required=True, 
#         default=1, 
#         type=openapi.TYPE_NUMBER
#         )
#     # custom response schema 
#     error_field = openapi.Schema( 
#         'error', 
#         description='this is a error string.', 
#         type=openapi.TYPE_STRING ) 
#     detail_field = openapi.Schema( 
#         'detail', 
#         description='this is a detail string.', 
#         type=openapi.TYPE_STRING ) 
#     code_field = openapi.Schema( 
#         'code', 
#         description='this is a code number.', 
#         type=openapi.TYPE_INTEGER ) 
#     error_resp = openapi.Schema( 
#         'response', 
#         type=openapi.TYPE_OBJECT, 
#         properties={ 
#             'error': error_field, 
#             'detail': detail_field, 
#             'code': code_field 
#         } 
#     )

#     @swagger_auto_schema(
#         manual_parameters=[mbtiId], 
#         responses={
#             200: 'success', 
#             400: 'this is a test description.', 
#             500: error_resp 
#         }
#     )
   
#     def get(self, request, format=None):
#         print(request)
#         mbtiId = request.GET.get("mbtiId", None)
#         queryset = Mbti.objects.filter(id=mbtiId)
#         serializer = MbtiSerializer(queryset, many=True)
#         return Response(serializer.data)
