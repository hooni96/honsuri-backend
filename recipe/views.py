from django.shortcuts import render

from .serializers import RecipeMainSerializer, RecipeDetailSerializer
from recipe.models import Recipe # 선언한 모델 import
from rest_framework import generics
# from rest_framework import viewsets # vieset import

class RecipeMainView(generics.ListAPIView): 
    queryset = Recipe.objects.all() 
    serializer_class = RecipeMainSerializer 

class RecipeDetailView(generics.RetrieveAPIView): 
    queryset = Recipe.objects.all() 
    serializer_class = RecipeDetailSerializer 