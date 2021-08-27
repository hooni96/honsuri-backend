from django.urls import path
from .views import *

app_name = 'mypage'

urlpatterns = [
    path('mypage/my-favorite', MyFavoriteView.as_view(), name='myfavorite'),
]