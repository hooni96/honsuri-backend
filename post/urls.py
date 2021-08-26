from django.urls import path
from . import views

urlpatterns =[
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view()),
    path('post/like/<int:pk>', views.LikePostView.as_view(), name='like'),
    path('comment/', views.CommentPost.as_view()),
    path('comment/<int:post_id>', views.CommentGet.as_view()),
    path('comment/<int:pk>', views.CommentDelete.as_view()),
]
