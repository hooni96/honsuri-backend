from django.shortcuts import render
from .serializers import MbtiSerializer 
from mbti.models import Mbti 
from rest_framework import generics
from rest_framework.permissions import AllowAny

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
