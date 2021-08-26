#APIView 사용하기 위해 import
from django.core import paginator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import filters
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .serializers import CommentSerializer, PostSerializer
from .models import Post, Comment

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes
from drf_yasg import openapi

class PostList(APIView): 
    # 방명록 작성 시작
    image=openapi.Parameter(
                            name="image",
                            in_=openapi.IN_FORM,
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_FILE),
                            # required=True,
                            description="Document"
                            )
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(request_body=PostSerializer, manual_parameters = [image])
    def post(self, request):
        '''
        방명록 작성
        '''
        serializer = PostSerializer(data=request.data, context={"request": request})
        #유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #방명록 리스트 시작
    keyword=openapi.Parameter(
                            name="keyword",
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING
                            )
    page=openapi.Parameter(
                            name="page",
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_INTEGER
                            )
    @swagger_auto_schema(manual_parameters = [keyword, page])
    def get(self, request):
        '''
        방명록 리스트 전체 조회 및 키워드 검색 
        '''
        keyword = request.GET.get('keyword', None)
        page = request.GET.get('page', None)
        posts = Post.objects.filter(content__contains=keyword).distinct() if keyword else Post.objects.all()
        paginator = Paginator(posts, 9)
        try:
            posts_page = paginator.page(page)
        except PageNotAnInteger:
            posts_page = paginator.page(1)
        except EmptyPage:
            posts_page = paginator.page(paginator.num_pages)
        Serializer = PostSerializer(posts_page, many=True)
        print(Serializer.data)


        return Response(Serializer.data)

#방명록 삭제 시작
class PostDelete(APIView): 
    @swagger_auto_schema(manual_parameters = [])
    def delete(self, request, id):
        '''
        방명록 게시물 삭제 
        '''
        posts = Post.objects.get(id=id)
        posts.delete()
        return Response("post delete", status=status.HTTP_200_OK)


class CommentPost(APIView): 
    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        '''
        댓글 작성
        '''
        serializer = CommentSerializer(data=request.data, context={"request": request})
        #유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentGet(APIView): 
    @swagger_auto_schema(manual_parameters = [])
    def get(self, request, post_id):
        #댓글 리스트 시작
        '''
        방명록 리스트 전체 조회 및 키워드 검색 
        '''
        comments = Comment.objects.get(post=post_id)
        Serializer = CommentSerializer(comments, many=True)

        return Response(Serializer.data)

#방명록 삭제 시작
class CommentDelete(APIView): 
    @swagger_auto_schema(manual_parameters = [])
    def delete(self, request, pk):
        '''
        방명록 게시물 삭제 
        '''
        comments = Comment.objects.get(pk=pk)
        comments.delete()
        return Response("comment delete", status=status.HTTP_200_OK)

