from rest_framework import serializers # serializer import
from .models import Post # 선언한 모델 import
from drf_yasg import openapi

# ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있음
# Post 작성, 리스트에 사용되는 Serialzier
class PostSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Post
        fields = '__all__'