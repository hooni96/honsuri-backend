#APIView 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import filters

from .serializers import PostImageSerializer, PostSerializer, PostUpdateSerializer
from .models import Post, PostImage

from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.utils import timezone

class PostList(APIView): 
    permission_classes = [AllowAny]

    @swagger_auto_schema(manual_parameters = [openapi.Parameter(name="keyword", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)])
    def get(self, request):
        '''
        방명록 리스트 전체 조회 및 키워드 검색 API
        '''
        keyword = request.GET.get('keyword', None)
        posts = Post.objects.filter(content__contains=keyword).distinct() if keyword else Post.objects.all()
        Serializer = PostSerializer(posts, many=True)
        return Response(Serializer.data)


    image=openapi.Parameter(name="image", in_=openapi.IN_FORM, type=openapi.TYPE_ARRAY, 
                            items=openapi.Items(type=openapi.TYPE_FILE), required=True, description="Document")
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(request_body=PostSerializer, manual_parameters = [image])
    def post(self, request):
        '''
        방명록 작성 API
        '''
        if request.user.is_authenticated:
            user_id = request.user.pk
            serializer = PostSerializer(data=request.data, context={"request": request})
            #유효성 검사
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView): 
    def delete(self, request, pk):
        '''
        방명록 게시물 삭제 
        '''
        user_id = request.user.pk
        if Post.objects.get(id=pk, user_id=user_id):
            Post.objects.get(id=pk).delete()
            return Response("post deleted", status=status.HTTP_200_OK)
        else:
            return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PostUpdateSerializer)
    def patch(self, request, pk): # 인스타처럼 이미지는 수정 불가능
        '''
        방명록 게시물 업데이트
        '''
        user_id = request.user.pk
        if Post.objects.get(id=pk, user_id=user_id):
            update_post = Post.objects.get(id=pk)
            update_post.content = request.data['content']
            update_post.updated_at = timezone.now()
            update_post.save()
            return Response("post updated", status=status.HTTP_200_OK)
        else:
            return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)

# class CommentList(ModelViewSet): 
#     '''
#     def Post: 댓글 작성
#     def Get: 댓글 리스트
#     ---
#     '''
#     queryset = Comment.objects.all() 
#     serializer_class = PostSerializer 

# class LikeView(APIView): 
#     '''
#     def Post: 좋아요 누르기/취소
#     ---
#     '''
#     queryset = Like.objects.all() 
#     serializer_class = PostSerializer 