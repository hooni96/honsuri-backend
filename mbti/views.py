from django.shortcuts import render
from .serializers import *
from mbti.models import Mbti 
from recipe.models import Recipe
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class MbtiView(generics.RetrieveAPIView): 
    '''
    mbti 질문과 보기를 반환하는 api
    ___
    파라미터: path로 질문 id 전달
    결과: mbti 질문과 보기(json) 반환
      - 보기의 key는
        - mbti 관련 질문일 경우: 해당 mbti 요소
        - mbti 무관 질문일 경우: A,B,C,D
    '''
    permission_classes = [AllowAny]
    queryset = Mbti.objects.all() 
    serializer_class = MbtiSerializer 

class MbtiResultView(APIView): 
    '''
    mbti 결과를 반환하는 api
    ___
    파라미터: query로 mbti 전달
    결과: cocktail(이름, id, 사진파일명), 문구 반환
    '''
    permission_classes = [AllowAny]
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('mbti', in_ = openapi.IN_QUERY,type=openapi.TYPE_STRING)])
    def get(self, request):
      mbti = request.GET.get('mbti')
      queryset = MbtiResult.objects.filter(mbti__contains=mbti)
      serializer = MbtiResultSerializer(queryset, many=True) 
      return Response(serializer.data)