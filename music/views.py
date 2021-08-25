from django.shortcuts import render
from .serializers import MusicSerializer 
from music.models import Music
from rest_framework import generics
from rest_framework.permissions import AllowAny

class MusicView(generics.ListAPIView):
    '''
    music 타이틀, 가수, 사진이름, 음원파일명을 반환하는 api
    ___
    파라미터: 없음
    결과: music 관련 정보 반환
      - id, 노래제목, 커버사진, 가수, mp3파일제목
    '''
    permission_classes = [AllowAny]
    queryset = Music.objects.all() 
    serializer_class = MusicSerializer
