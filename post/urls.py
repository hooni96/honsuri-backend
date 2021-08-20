from django.urls import path
from . import views

urlpatterns =[
    path('post/', views.PostList.as_view()),
]
