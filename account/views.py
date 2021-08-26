from django.http.response import JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import UserCreateSerializer, UserLoginSerializer, UserSerializer
from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

@permission_classes([AllowAny])
class RegisterView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    '''
    회원가입 api
    ---
    '''
    def post(self, request, formet=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class Login(GenericAPIView):
    serializer_class = UserLoginSerializer
    '''
    로그인 api
    ---
    파라미터: email, password
    결과: id, token 반환
    '''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['id'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                 "id": UserSerializer(
                     user,context=self.get_serializer_context()
                 ).data.get('id'), 
                 "token": user['token']
             }
        )