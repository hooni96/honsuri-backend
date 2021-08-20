from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정
router.register('recipe', views.RecipeViewSet)  # ViewSet과 함께 recipe라는 router 등록

urlpatterns = [
    path('', include(router.urls)),
]