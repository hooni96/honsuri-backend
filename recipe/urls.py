from django.urls import include, path
# from rest_framework import routers  # router import
# from . import views  # views.py import
from .views import *



urlpatterns = [
    path('recipes', RecipeMainView.as_view(), name='recipes'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipes/<int:pk>/bookmark', BookmarkView.as_view(), name='bookmark'), #  
]