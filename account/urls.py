from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views

app_name = 'account'

urlpatterns = [
    path('account/register/', views.RegisterView.as_view()),
    path('account/login/', obtain_jwt_token),
    path('account/logout/', refresh_jwt_token),
    ]