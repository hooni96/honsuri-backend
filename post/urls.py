from django.urls import path
from . import views

urlpatterns =[
    path('post/', views.PostList.as_view()),
    path('post/<int:id>', views.PostDelete.as_view()),
    path('comment/', views.CommentPost.as_view()),
    path('comment/<int:post_id>', views.CommentGet.as_view()),
    path('comment/<int:pk>', views.CommentDelete.as_view()),
]
