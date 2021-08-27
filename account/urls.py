from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views

app_name = 'account'

urlpatterns = [
    path('account/register', views.RegisterView.as_view()),
    path('account/login', views.Login.as_view()),
    path('account/email-find', views.EmailFindView.as_view()),
    ]