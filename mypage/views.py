from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
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
  
  @swagger_auto_schema(request_body=UserUpdateSerializer)
  def patch(self, request):
      '''
      회원수정 api
      ---
      결과: 나의정보(이름,닉네임,연락처), 관심정보(주량,최애술,최애안주,최애콤비) 수정 후 저장
      '''
      user_id = request.user.pk
      try:
        update_user = User.objects.get(id = user_id)
        update_user.name = request.data['name']
        update_user.nickname = request.data['nickname']
        update_user.phone_number = request.data['phone_number']
        update_user.alcohol_amount = request.data['alcohol_amount']
        update_user.favorite_alcohol = request.data['favorite_alcohol']
        update_user.favorite_food = request.data['favorite_food']
        update_user.favorite_combination = request.data['favorite_combination']
        update_user.save()
        return Response("user updated", status=status.HTTP_200_OK)

      except:
        return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request):
      '''
      회원탈퇴 api
      ---
      결과: 메시지 반환
      '''
      user_id = request.user.pk
      try:
        User.objects.get(id = user_id).delete()
        return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
      except:
        return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

"""
    @swagger_auto_schema(request_body=PostUpdateSerializer)
    def patch(self, request, pk): # 인스타처럼 이미지는 수정 불가능
        '''
        방명록 게시물 업데이트
        '''
        user_id = request.user.pk
        if Post.objects.get(id=pk, user_id=user_id):
            update_post = Post.objects.get(id=pk)
            update_post.content = request.data['content']
            update_post.updated_at = timezone.now()
            update_post.save()
            return Response("post updated", status=status.HTTP_200_OK)
        else:
            return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)
"""


    