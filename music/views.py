from django.shortcuts import render

from .serializers import MusicSerializer # 생성한 serializer import
from music.models import Music # 선언한 모델 import
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

class MusicView(generics.ListAPIView):
    '''
    music 타이틀, 가수, 사진이름, 음원파일명을 반환하는 api
    ---
    '''
    permission_classes = [
        AllowAny
    ]
    queryset = Music.objects.all() 
    serializer_class = MusicSerializer
