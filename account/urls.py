from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('account/register', views.RegisterView.as_view()),
    path('account/login', views.Login.as_view()),
    path('account/email-find', views.EmailFindView.as_view()),
    ]