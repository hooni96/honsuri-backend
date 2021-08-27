from django.shortcuts import render
from recipe.models import Recipe
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

class MyPostView(APIView):
    '''
    내가 북마크한 레시피 api
    ---
    결과: 좋아요한 레시피(아이디,사진,이름,태그요소들) 반환
    '''

    permission_classes = [AllowAny]

    def get(self, request):
        '''
        방명록 리스트 전체 조회 및 키워드 검색 API
        '''       
        # keyword에 따른 queryset 필터링
        post_list = []
        
        # 로그인 여부에 따른 좋아요 여부 추가파트
        if request.user.is_authenticated: # 로그인 되어 있을 경우
            user_id = request.user.pk
            queryset = Post.objects.filter(user_id=[user_id])
            serializer = PostSerializer(queryset, many=True)
            for each in serializer.data:
                each['like_count'] = LikePost.objects.filter(post_id=each['id']).count()
                each['comment_count'] = Comment.objects.filter(post_id=each['id']).count()

                each['likepost'] = True if int(user_id) in each['likepost'] else False
                post_list.append(each)           
        return Response(post_list)

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