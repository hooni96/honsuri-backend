from rest_framework import serializers # serializer import
from recipe.models import * # 선언한 모델 import
from drf_yasg import openapi

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ("name",)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("name",)

class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ("name",)

class AlcoholVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlcoholVolume
        fields = ("name",)

# class BookmarkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = "recipe_bookmark"
#         fields = ("user_id","recipe_id",)

class RecipeMainSerializer(serializers.ModelSerializer): 
    base = BaseSerializer(read_only=True, many=True)
    ingredient = IngredientSerializer(read_only=True, many=True)
    alcohol_volume = FlavorSerializer(read_only=True, many=True)
    flavor = AlcoholVolumeSerializer(read_only=True, many=True)
    class Meta:
        model = Recipe  # 모델 설정
        fields = (
            "id",
            "name",
            "photo",
            "base",
            "ingredient",
            "alcohol_volume",
            "flavor",
            "bookmark",
        )

class RecipeDetailSerializer(serializers.ModelSerializer): 
    base = BaseSerializer(read_only=True, many=True)
    ingredient = IngredientSerializer(read_only=True, many=True)
    alcohol_volume = FlavorSerializer(read_only=True, many=True)
    flavor = AlcoholVolumeSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe  # 모델 설정
        fields = (
            "id",
            "name",
            "photo",
            "how_to_mix",
            "detail_contents",
            "youtube_link",
            "base",
            "ingredient",
            "alcohol_volume",
            "flavor",
            "bookmark",
        )