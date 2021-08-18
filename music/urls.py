from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()  # DefaultRouter 설정
router.register('music', views.MusicViewSet)  # ViewSet과 함께 mbti라는 router 등록

urlpatterns = [
    path('', include(router.urls)),
]