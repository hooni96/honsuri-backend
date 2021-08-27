from django.shortcuts import render
from recipe.models import Recipe
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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
    @swagger_auto_schema(request_body=EmailFindSerializer)
    def patch(self, request):
      user_id = request.user.pk
      # 로그인 기능 이용해서 있는 비밀번호인지 확인하고
      serializer = PasswordSerializer(data = request.data)
      # 회원가입 기능 이용해서 새로운 비밀번호 등록
      queryset = User.objects.filter(id = user_id)
      serializer = UserSerializer(queryset, many=True) 

      return Response(serializer.data[0])