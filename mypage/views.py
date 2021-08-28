from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer
from recipe.models import Recipe
from account.models import User
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password



class MyPostView(APIView):
    def get(self, request):
        '''
        내가 작성한 글 조회 API
        ---
        결과: 내가 작성한 글 정보 리스트로 반환
        '''       
        post_list = []
        
        user_id = request.user.pk
        queryset = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(queryset, many=True)
        for each in serializer.data:
            each['like_count'] = LikePost.objects.filter(post_id=each['id']).count()
            each['comment_count'] = Comment.objects.filter(post_id=each['id']).count()
            post_list.append(each)           
        return Response(post_list)


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
        queryset = User.objects.filter(id = user_id)
        serializer = UserSerializer(queryset, many=True) 
        return Response(serializer.data[0], status=status.HTTP_200_OK)
      except:
        return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)

  @swagger_auto_schema(request_body=UserDeleteSerializer)
  def delete(self, request):
      '''
      회원탈퇴 api
      ---
      결과: 메시지 반환 {'message': 'DELETED'}
      '''
      user_id = request.user.pk
      password = request.data['password']
      if check_password(password,request.user.password):
        User.objects.get(id = user_id).delete()
        return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
      else:
        return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

      

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
