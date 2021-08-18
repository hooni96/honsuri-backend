from django.shortcuts import render

from rest_framework import viewsets # vieset import
from .serializers import MusicSerializer # 생성한 serializer import
from music.models import Music # 선언한 모델 import

class MusicViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Music.objects.all() 
    serializer_class = MusicSerializer