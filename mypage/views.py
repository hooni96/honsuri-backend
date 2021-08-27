from django.shortcuts import render
from recipe.models import Recipe
from account.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate


class MyFavoriteView(APIView): 
    '''
    내가 북마크한 레시피 api
    ---
    결과: 좋아요한 레시피(아이디,사진,이름,태그요소들) 반환
    '''
    def get(self, request):
      user_id = request.user.pk

      queryset = Recipe.objects.filter(bookmark__in=[user_id])
      serializer = MyFavoriteSerializer(queryset, many=True) 

      return Response(serializer.data)

class MyPageView(APIView): 
    '''
    나의 정보 api
    ---
    결과: 나의정보(이메일,이름,닉네임,연락처), 관심정보(주량,최애술,최애안주,최애콤비) 반환
    '''
    def get(self, request):
      user_id = request.user.pk
      queryset = User.objects.filter(id = user_id)
      serializer = UserSerializer(queryset, many=True) 

      return Response(serializer.data[0])

class PasswordView(APIView): 
    '''
    Password 변경 api
    ---
    파라미터: request body로 현재 비밀번호, 새 비밀번호, 새 비밀번호(확인) 입력
    결과: 성공여부 메시지 반환
    '''
    @swagger_auto_schema(request_body=PasswordSerializer)
    def patch(self, request):
      if request.data['new_password1'] == request.data['new_password2']:
        user_email = request.user.email
        password = request.data['password']
        user = authenticate(email=user_email, password=password)

        # 현재 비밀번호가 맞지 않으면
        if user is None:
          return Response({'message':'WRONG_PASSWORD'}, status=status.HTTP_400_BAD_REQUEST)
        else:
          # 새로운 비밀번호 등록
          user.set_password(request.data['new_password1'])
          user.save()
          return Response({'message':'PASSWORD_UPDATE'}, status=status.HTTP_201_CREATED)
      else:
          return Response({'message':'NOT_MATHCING_PASSWORD'}, status=status.HTTP_400_BAD_REQUEST)
