from django.shortcuts import render

from .serializers import RecipeMainSerializer, RecipeDetailSerializer, BookmarkSerializer
from recipe.models import * # 선언한 모델 import
from rest_framework import status, generics
# from rest_framework import viewsets # vieset import
from rest_framework.response import Response

class RecipeMainView(generics.ListAPIView): 
    queryset = Recipe.objects.all() 
    serializer_class = RecipeMainSerializer 

class RecipeDetailView(generics.RetrieveAPIView): 
    queryset = Recipe.objects.all() 
    serializer_class = RecipeDetailSerializer 

# user_id는 jwt token에서 받아오도록 수정할 예정
class BookmarkView(generics.CreateAPIView): 
    model = Bookmark
    serializer_class = BookmarkSerializer 

    def post(self, request, pk):
        '''
        북마크가 존재하면 삭제, 없으면 생성
        '''
        recipe_id = pk
        user_id = request.data['user_id']
        user = User.objects.get(id = user_id)
        recipe = Recipe.objects.get(id = recipe_id)

        if Bookmark.objects.filter(recipe_id=recipe_id, user_id=user_id).exists():
            Bookmark.objects.get(recipe_id=recipe_id, user_id=user_id).delete()
            return Response({'message': 'DELETE_BOOKMARK'}, status=200)
        else:
            Bookmark.objects.create(user_id=user, recipe_id=recipe).save
            return Response({'message': 'CREATE_BOOKMARK'}, status=200)

        
