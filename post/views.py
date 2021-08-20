from django.http import HttpResponse
from django.shortcuts import render

from .serializers import PostSerializer
from .models import Post, Comment, Like
      
from django.shortcuts import get_object_or_404

class PostViewSet(ModelViewSet): 
    '''
    def Post: 방명록 작성 api
    def Get: 방명록 리스트 
    def Get: 방명록 검색
    ---
    '''
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 


# class LikeView(ModelViewSet): 
#     '''
#     def Post: 좋아요 누르기/취소
#     ---
#     '''
#     queryset = Like.objects.all() 
#     serializer_class = PostSerializer 

# class CommentView(ModelViewSet): 
#     '''
#     def Post: 댓글 작성
#     def Get: 댓글 리스트
#     ---
#     '''
#     queryset = Comment.objects.all() 
#     serializer_class = PostSerializer 