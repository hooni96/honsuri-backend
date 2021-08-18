from django.urls import include, path
from rest_framework import routers  # router import
from .views import MbtiView  

# router = routers.DefaultRouter()  # DefaultRouter 설정
# router.register('mbti', views.MbtiViewSet)  # ViewSet과 함께 mbti라는 router 등록

app_name = 'mbti'

urlpatterns = [
    path('mbti/<int:pk>/', MbtiView.as_view(), name='mbti'),
]