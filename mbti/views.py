from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets # vieset import
from .serializers import MbtiSerializer # 생성한 serializer import
from mbti.models import Mbti # 선언한 모델 import

# def helloworld(request):
#     return HttpResponse('hello world!')

class MbtiViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Mbti.objects.all() # 존재하는 테이블의 데이터를 전부 가져오겠다는 뜻
    serializer_class = MbtiSerializer # 이전에 생성하였던 MbtiSerializer 클래스를 이용하겠다는 뜻