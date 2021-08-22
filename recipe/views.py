from django.shortcuts import render, get_object_or_404

from .serializers import *
from recipe.models import * # 선언한 모델 import
from rest_framework import status, generics
from rest_framework.views import APIView
# from rest_framework import viewsets # vieset import
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RecipeMainView(APIView):
    '''
    레시피 메인에 레시피 리스트 반환하는 API
    ---
    base 옵션이 있을 경우 필터링해서 출력
    base=1 소주
    base=2 양주
    base=3 맥주
    base=4 와인
    base=5 과일소주
    '''
    base = openapi.Parameter('base',
                            in_ = openapi.IN_QUERY,
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_STRING),
                            collection_format = "multi"
                            )
    @swagger_auto_schema(manual_parameters=[base])
    def get(self, request):
        base = request.GET.getlist('base', None)
        if base:
            queryset = Recipe.objects.filter(base__in=base).distinct()
            serializer = RecipeMainSerializer(queryset, many=True) 
        else:
            queryset = Recipe.objects.all() 
            serializer = RecipeMainSerializer(queryset, many=True) 
        return Response(serializer.data)        
            
class RecipeDetailView(generics.RetrieveAPIView): 
    '''
    레시피 id에 따라 레시피 디테일 정보를 반환하는 API 
    '''
    queryset = Recipe.objects.all() 
    serializer_class = RecipeDetailSerializer 

# user_id는 jwt token에서 받아오도록 수정할 예정
class BookmarkView(APIView): 
    user_pk = openapi.Parameter('user_pk', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(manual_parameters=[user_pk])
    def post(self, request, pk):
        '''
        북마크가 존재하면 삭제, 없으면 생성
        ---
        레시피 id는 url path로 전달
        user_id는 jwt_token 으로 받아올 예정(이지만 아직 jwt_token 기능이 없어서 query로 받는 중)
        '''
        recipe = get_object_or_404(Recipe, pk=pk)
        
        # recipe_id = pk
        user_id = request.GET.get('user_pk')
        # user = User.objects.get(id = user_id)
        # recipe = Recipe.objects.get(id = recipe_id)

        print('-'*50)
        print(recipe.bookmark)
        print('-'*50)

        if user_id in recipe.bookmark.all():
            recipe.bookmark.remove(user_id)
            return Response({'message': 'DELETE_BOOKMARK'}, status=status.HTTP_200_OK)
        else:
            recipe.bookmark.add(user_id)
            return Response({'message': 'CREATE_BOOKMARK'}, status=status.HTTP_200_OK)

        # if Bookmark.objects.filter(recipe_id=recipe_id, user_id=user_id).exists():
        #     Bookmark.objects.get(recipe_id=recipe_id, user_id=user_id).delete()
        #     return Response({'message': 'DELETE_BOOKMARK'}, status=status.HTTP_200_OK)
        # else:
        #     Bookmark.objects.create(user_id=user, recipe_id=recipe).save
        #     return Response({'message': 'CREATE_BOOKMARK'}, status=status.HTTP_200_OK)

        
