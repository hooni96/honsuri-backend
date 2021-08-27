from django.shortcuts import render
from rest_framework import status
from recipe.models import Recipe
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class MyFavoriteView(APIView): 
  def get(self, request):
    '''
    내가 북마크한 레시피 api
    ---
    결과: 좋아요한 레시피(아이디,사진,이름,태그요소들) 반환
    '''
    user_id = request.user.pk

    queryset = Recipe.objects.filter(bookmark__in=[user_id])
    serializer = MyFavoriteSerializer(queryset, many=True) 

    return Response(serializer.data)

class MyPageView(APIView): 
  def get(self, request):
      '''
      나의 정보 api
      ---
      결과: 나의정보(이메일,이름,닉네임,연락처), 관심정보(주량,최애술,최애안주,최애콤비) 반환
      '''
      user_id = request.user.pk
      queryset = User.objects.filter(id = user_id)
      serializer = UserSerializer(queryset, many=True) 

      return Response(serializer.data[0])

  def delete(self, request):
      '''
      유저 id 받아서 회원탈퇴 api
      ---
      결과: 메시지 반환
      '''
      user_id = request.user.pk
      try:
        User.objects.get(id = user_id).delete()
        return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
      except:
        return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)