from django.urls import path
from .views import MbtiView  

app_name = 'mbti'

urlpatterns = [
    path('mbti/<int:pk>/', MbtiView.as_view(), name='mbti'),
]