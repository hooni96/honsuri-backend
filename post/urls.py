from django.urls import path
from . import views


urlpatterns =[
    path('post', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view()),
    path('post/like/<int:pk>', views.LikePostView.as_view(), name='like'),
    path('post/<int:post_id>/comment', views.CommentGetPost.as_view()),
    path('post/comment/<int:comment_id>', views.CommentDelete.as_view()),
]