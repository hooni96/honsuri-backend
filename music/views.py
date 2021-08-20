from django.shortcuts import render

from .serializers import MusicSerializer # 생성한 serializer import
from music.models import Music # 선언한 모델 import
from rest_framework import generics

class MusicView(generics.ListAPIView):
    queryset = Music.objects.all() 
    serializer_class = MusicSerializer
