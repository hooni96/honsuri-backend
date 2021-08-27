from rest_framework import serializers
from recipe.models import * 
from recipe.serializers import BaseSerializer, IngredientSerializer, FlavorSerializer, AlcoholVolumeSerializer
from account.models import User 
from django.contrib.auth import authenticate

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


# ---------------------------------------------------------------------------------------------------------------------
class PasswordSerializer(serializers.ModelSerializer):
    new_password1 = serializers.CharField(max_length=128, write_only=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True)

    def validate(self, validated_data):
        # 현재 비밀번호 확인
        user_id = self.context['request'].user.pk
        user_email = User.objects.filter(id = user_id).values_list('email',)[0]
        password = validated_data['password']
        user = authenticate(email=user_email, password=password)

        # 현재 비밀번호가 맞지 않으면
        if user is None:
            return {'id': 'None'}
        else:
            # 새로운 비밀번호 등록
            user.set_password(validated_data['new_password1'])
            user.save()
            return user
    class Meta:
        model = User
        fields = ['password','new_password1','new_password2']


    
