from rest_framework import serializers # serializer import
from music.models import Music # 선언한 모델 import

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music  # 모델 설정
        fields = ['id','title','photo','singer','file_name']  # 필드 설정