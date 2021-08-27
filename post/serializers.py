from rest_framework import serializers # serializer import
from .models import * # 선언한 모델 import
from drf_yasg import openapi

# ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있음
# Post 작성, 리스트에 사용되는 Serialzier
class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ("image",)

class PostSerializer(serializers.ModelSerializer):  
    photos = PostImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ( "id", "photos", "content", "created_at","user_id", )
        read_only_fields = ("id", "created")
        # 좋아요 추가
        extra_kwargs = {'likepost': {'required': False}}

    def create(self, validated_data):
        user_id =  self.context['request'].user.pk
        image_set = self.context['request'].FILES
        instance = Post.objects.create(
            user_id=user_id,
            content=validated_data['content']
            )
        for image_data in image_set.getlist("image"):
            PostImage.objects.create(post=instance, image=image_data)
        return instance

class PostUpdateSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Post
        fields = ("content",)

class LikeSerializer(serializers.ModelSerializer):
    post_id = PostSerializer(read_only = True)
    class Meta:
        model = LikePost
        fields =['id', 'user_id', 'post_id']

class PostLikeSerializer(serializers.ModelSerializer):  
    photos = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ( "id", "photos", "content", "created_at","user_id","likepost", )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "post", "content", "created_at",)
        read_only_fields = ("id", "created", "post")
