from django.db.models import fields
from rest_framework import serializers
from recipe.models import * 
from recipe.serializers import BaseSerializer, IngredientSerializer, FlavorSerializer, AlcoholVolumeSerializer
from post.serializers import *
from post.models import *
from account.models import User 

#내가쓴글
class MyPostSerializer(serializers.ModelSerializer):
    post = PostImageSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ( "id", "photos", "content", "created_at", "user_id", )
        read_only_fields = ("id", "created_at")
        # 좋아요 추가
        extra_kwargs = {'likepost': {'required': False}}

#내가좋아하는 레시피
class MyFavoriteSerializer(serializers.ModelSerializer): 
    base = BaseSerializer(read_only=True, many=True)
    ingredient = IngredientSerializer(read_only=True, many=True)
    alcohol_volume = FlavorSerializer(read_only=True, many=True)
    flavor = AlcoholVolumeSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "photo",
            "base",
            "ingredient",
            "alcohol_volume",
            "flavor"]
        read_only_fields = ["bookmark"]

#사용자
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'nickname', 'phone_number', 
        'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination']
