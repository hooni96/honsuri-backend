from rest_framework import serializers
from mbti.models import Mbti, MbtiResult
from recipe.models import Recipe

class MbtiSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Mbti 
        fields = ['id','question','answer'] 

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe 
        fields = ['id','name','photo'] 


class MbtiResultSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only = True)
    class Meta:
        model = MbtiResult 
        fields = ['id','mbti','comment','recipe'] 