from rest_framework import serializers
from recipe.models import * 
from recipe.serializers import BaseSerializer, IngredientSerializer, FlavorSerializer, AlcoholVolumeSerializer
from account.models import User 

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'nickname', 'phone_number', 
        'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'nickname', 'phone_number', 
        'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination']
