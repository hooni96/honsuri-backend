from django.urls import path
from . import views

urlpatterns =[
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDelete.as_view()),
]
