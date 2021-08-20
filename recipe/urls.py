from django.urls import include, path
# from rest_framework import routers  # router import
# from . import views  # views.py import
from .views import RecipeMainView, RecipeDetailView, BookmarkView  



urlpatterns = [
    path('recipes', RecipeMainView.as_view(), name='recipe_main'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipes_detail'),
    path('recipes/<int:pk>/bookmark', BookmarkView.as_view(), name='bookmark'), #  
]