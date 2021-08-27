#APIView 사용하기 위해 import
from django.core import paginator
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
=======
from rest_framework import status
>>>>>>> b7bbc2e1b3b72a8749900c7997405d7702426855
from django.http import Http404
from rest_framework import filters
from rest_framework import generics
from .serializers import *
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
        # keyword에 따른 queryset 필터링
        keyword = request.GET.get('keyword', None)
        queryset = Post.objects.filter(content__contains=keyword).distinct() if keyword else Post.objects.all()
        serializer = PostSerializer(queryset, many=True)

        post_list = []
        
        # 로그인 여부에 따른 좋아요 여부 추가파트
        if request.user.is_authenticated: # 로그인 되어 있을 경우
            user_id = request.user.pk
            serializer = PostLikeSerializer(queryset, many=True)
            for each in serializer.data:
                each['like_count'] = LikePost.objects.filter(post_id=each['id']).count()
                each['comment_count'] = Comment.objects.filter(post_id=each['id']).count()

                each['likepost'] = True if int(user_id) in each['likepost'] else False
                post_list.append(each)
        else:
            for each in serializer.data:
                each['like_count'] = LikePost.objects.filter(post_id=each['id']).count()
                each['comment_count'] = Comment.objects.filter(post_id=each['id']).count()
                post_list.append(each)            
        return Response(post_list)


    image=openapi.Parameter(name="image", in_=openapi.IN_FORM, type=openapi.TYPE_ARRAY, 
                            items=openapi.Items(type=openapi.TYPE_FILE), required=True, description="Document")
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(request_body=PostSerializer, manual_parameters = [image])
    def post(self, request):
        '''
        방명록 작성 API
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
            return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

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

class LikePostView(APIView):
    model = LikePost
    serializer_class = LikeSerializer

    def post(self, request, pk, format=None):
        '''
        게시글의 좋아요 상태를 추가,삭제하는 api
        
        return : 생성, 삭제 여부 메시지
        '''
        if not LikePost.objects.filter(post_id=pk, user_id=request.user.pk).exists():
            LikePost.objects.create(
                user_id=request.user,
                post_id=Post.objects.get(id=pk)
            ).save
            return Response({'message': 'CREATE_LIKE_POST'}, status.HTTP_200_OK)

        delete_post = LikePost.objects.get(post_id=pk, user_id=request.user.pk)
        delete_post.delete()
        return Response({'message': 'DELETE_LIKE_POST'}, status.HTTP_200_OK)

# ---------------------------------------------------------------------------------------
# 덧글 API
# ---------------------------------------------------------------------------------------
class CommentGetPost(APIView): 
    permission_classes = [AllowAny]
    @swagger_auto_schema(tags=['comment'])
    def get(self, request, post_id):
        '''
        POST ID로 댓글 전체 읽어오기
        '''
        comments = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CommentSerializer, tags=['comment'])
    def post(self, request, post_id):
        '''
        댓글 작성
        '''
        if request.user.is_authenticated: 
            Comment.objects.create(
                    user_id = request.user.pk,
                    post_id = post_id,
                    content = request.data['content']
                ).save
            return Response({'message': 'POST_SUCCESS'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'NOT_LOGGEDIN'}, status=status.HTTP_400_BAD_REQUEST)

class CommentDelete(APIView): 
    @swagger_auto_schema(tags=['comment'])
    def delete(self, request, comment_id):
        '''
        덧글 id 입력받아 삭제 
        '''
        user_id = request.user.pk
        if Comment.objects.get(id=comment_id, user_id=user_id): # 본인 덧글이면
            Comment.objects.get(id=comment_id).delete()
            return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CommentSerializer, tags=['comment'])
    def patch(self, request, comment_id): 
        '''
        방명록 게시물 업데이트
        '''
        user_id = request.user.pk
        if Comment.objects.get(id=comment_id, user_id=user_id): # 본인 덧글이면
            update_comment = Comment.objects.get(id=comment_id)
            update_comment.content = request.data['content']
            update_comment.updated_at = timezone.now()
            update_comment.save()
            return Response({'message': 'UPDATED'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)
