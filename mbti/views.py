from django.shortcuts import render

from .serializers import MbtiSerializer # 생성한 serializer import
from mbti.models import Mbti # 선언한 모델 import
from rest_framework import generics

class MbtiView(generics.RetrieveAPIView): 
    '''
    mbti 질문과 보기를 반환하는 api
    ---
    '''
    queryset = Mbti.objects.all() 
    serializer_class = MbtiSerializer 
