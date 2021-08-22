#APIView 사용하기 위해 import
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from .serializers import PostSerializer
from .models import Post

class PostList(APIView): 
    '''
    def Post: 방명록 작성 
    '''
    # 방명록 작성

    @swagger_auto_schema(request_body=PostSerializer)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={"request": request})
        #유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    def Post: 방명록 작성 
    '''
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    '''
    def Get: 방명록 리스트 검색 
    '''

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