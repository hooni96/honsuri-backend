from rest_framework.views import APIView
from mysite.settings import DATABASES
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import *
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
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@permission_classes([AllowAny])
class RegisterView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    '''
    mbti 질문과 보기를 반환하는 api
    ___
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

@permission_classes([AllowAny])
class EmailFindView(APIView): 
    '''
    아이디 찾기 api
    ---
    파라미터: 이름, 핸드폰번호 request body로 받아오기
    결과: 유저 이메일 리스트(여러개일 경우) 반환
    '''
    @swagger_auto_schema(request_body=EmailFindSerializer)
    def post(self, request):
        name = request.data['name']
        phone_number = request.data['phone_number']
        if User.objects.filter(name = name, phone_number=phone_number):
            queryset = User.objects.filter(phone_number = phone_number)
            serializer = EmailFindSerializer(queryset, many=True) 
            email_list=[]
            for each in serializer.data:
                email_list.append(each['email']) 
            return Response(email_list, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Wrong info"}, status=status.HTTP_401_UNAUTHORIZED)