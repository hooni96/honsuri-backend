from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets # vieset import
from .serializers import MbtiSerializer # 생성한 serializer import
from mbti.models import Mbti # 선언한 모델 import

# def helloworld(request):
#     return HttpResponse('hello world!')

class MbtiViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Mbti.objects.all()
    serializer_class = MbtiSerializer