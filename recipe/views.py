from django.shortcuts import render, get_object_or_404

from .serializers import *
from recipe.models import * # 선언한 모델 import
from rest_framework import status, generics
from rest_framework.views import APIView
# from rest_framework import viewsets # vieset import
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class RecipeMainView(APIView):
    '''
    레시피 메인에 레시피 리스트 반환하는 API
    ---
    base 옵션이 있을 경우 필터링해서 출력
    base=1 소주
    base=2 양주
    base=3 맥주
    base=4 와인
    base=5 과일소주
    '''
    permission_classes = [AllowAny]
    base = openapi.Parameter('base',
                            in_ = openapi.IN_QUERY,
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_STRING),
                            collection_format = "multi"
                            )
    @swagger_auto_schema(manual_parameters=[base])
    def get(self, request):
        base = request.GET.getlist('base', None)
        # base에 따른 queryset 필터링
        queryset = Recipe.objects.filter(base__in=base).distinct() if base else Recipe.objects.all()

        # 로그인 여부에 따른 북마크 추가파트
        if request.user.is_authenticated:
            user_id = request.user.pk
            serializer = RecipeMainSerializer(queryset, many=True) 
            # 북마크 추가파트
            recipe_list = []
            for each in serializer.data:
                if int(user_id) in each['bookmark']:
                    each['bookmark'] = True
                else:
                    each['bookmark'] = False
                recipe_list.append(each)

            return Response(recipe_list)
        else: # 로그인 안 되어 있을 경우
            serializer = RecipeMainSerializerNotLoggedin(queryset, many=True) 
            return Response(serializer.data)

class RecipeDetailView(APIView): 
    '''
    path에 있는 레시피 id에 따라 레시피 디테일 정보를 반환하는 API 
    '''
    permission_classes = [AllowAny]
    def get(self, request, pk):
        queryset = Recipe.objects.filter(id=pk)

        # 로그인 여부에 따른 북마크 추가파트
        if request.user.is_authenticated:
            user_id = request.user.pk
            serializer = RecipeDetailSerializer(queryset, many=True)
            # 북마크 추가파트
            if user_id in serializer.data[0]['bookmark']:
                serializer.data[0]['bookmark'] = True
            else:
                serializer.data[0]['bookmark'] = False
        else:
            serializer = RecipeDetailSerializerNotLoggedin(queryset, many=True)
        
        return Response(serializer.data)

# user_id는 jwt token에서 받아오도록 수정할 예정
class BookmarkView(APIView): 
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def post(self, request, pk):
        '''
        북마크가 존재하면 삭제, 없으면 생성
        ---
        레시피 id는 url path로 전달
        user_id는 jwt_token 으로 받아올 예정(이지만 아직 jwt_token 기능이 없어서 query로 받는 중)
        '''
        recipe = get_object_or_404(Recipe, pk=pk)
        user_id = request.user.pk
        user = User.objects.get(id = user_id)

        if user in recipe.bookmark.all():
            recipe.bookmark.remove(user_id)
            return Response({'message': 'DELETE_BOOKMARK'}, status=status.HTTP_200_OK)
        else:
            recipe.bookmark.add(user_id)
            return Response({'message': 'CREATE_BOOKMARK'}, status=status.HTTP_200_OK)

        
