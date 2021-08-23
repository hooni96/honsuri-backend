from rest_framework import serializers
from account.models import User, ALCOHOL
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

# 회원가입
class UserCreateSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="이미 존재하는 아이디 입니다.")])
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password', 'placeholder': 'Password'}, validators=[validate_password])
    name = serializers.CharField(write_only=True)
    nickname = serializers.CharField(write_only=True)
    phone_number = serializers.IntegerField(write_only=True)
    alcohol_amount = serializers.ChoiceField(choices=ALCOHOL)
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

    