from django.urls import include, path
from rest_framework import routers  # router import
from .views import MbtiView  

app_name = 'mbti'

urlpatterns = [
    path('mbti/<int:pk>/', MbtiView.as_view(), name='mbti'),
]