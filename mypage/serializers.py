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


# ---------------------------------------------------------------------------------------------------------------------
class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(validators=[validate_password])
    new_password1 = serializers.CharField(validators=[validate_password])
    new_password2 = serializers.CharField(validators=[validate_password])

    def validate(self, data):
        user_id =  self.context['request'].user.pk
        email = data.get("email")
        password = data.get("password", None)

        user = authenticate(email=email, password=password)

        if user is None:
            return {'id': 'None','email':email}
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'id':user.id,
            'token': jwt_token
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'new_password1', 'new_password2']


    
