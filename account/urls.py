from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.Login.as_view()),
    ]