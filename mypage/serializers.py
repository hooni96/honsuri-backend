from rest_framework import serializers
from recipe.models import * 
from recipe.serializers import BaseSerializer, IngredientSerializer, FlavorSerializer, AlcoholVolumeSerializer

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