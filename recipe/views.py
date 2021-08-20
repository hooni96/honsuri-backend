from django.shortcuts import render

from .serializers import RecipeSerializer # 생성한 serializer import
from recipe.models import Recipe # 선언한 모델 import
# from rest_framework import generics
from rest_framework import viewsets # vieset import

class RecipeViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Recipe.objects.all() 
    serializer_class = RecipeSerializer 
