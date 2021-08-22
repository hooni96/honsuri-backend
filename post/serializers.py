from rest_framework import serializers # serializer import
from .models import Post, PostImage # 선언한 모델 import
from drf_yasg import openapi

# ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있음
# Post 작성, 리스트에 사용되는 Serialzier
class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ("image",)

class PostSerializer(serializers.ModelSerializer):  
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('user_id', 'content', 'created_at', 'images',)
        read_only_fields = ("id", "created")

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist("image"):
            PostImage.objects.create(post_id=instance, image=image_data)
        return instance
