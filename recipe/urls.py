from django.urls import include, path
from .views import *

urlpatterns = [
    path('recipes', RecipeMainView.as_view(), name='recipes'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipes/<int:pk>/bookmark', BookmarkView.as_view(), name='bookmark'), #  
]