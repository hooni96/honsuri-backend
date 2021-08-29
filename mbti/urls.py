from django.urls import path
from .views import MbtiView, MbtiResultView


app_name = 'mbti'

urlpatterns = [
    path('mbti/qna', MbtiView.as_view(), name='mbti'),
    path('mbti', MbtiResultView.as_view(), name='mbti_result'),
]