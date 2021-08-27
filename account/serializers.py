from typing import AbstractSet
from rest_framework import serializers
from account.models import User
from drf_yasg import openapi
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from .models import *

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

# 기본 유저 모델 불러오기
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="이미 존재하는 아이디 입니다.")])
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password', 'placeholder': 'Password'}, validators=[validate_password])
    name = serializers.CharField(write_only=True)
    nickname = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()

    alcohol_amount = serializers.FloatField()
    favorite_alcohol = serializers.CharField()
    favorite_food = serializers.CharField()
    favorite_combination = serializers.CharField()
    token = serializers.SerializerMethodField()
    
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'nickname', 'phone_number', 'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination', 'token']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

class EmailFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone_number','email']
        read_only_fields = ['email']