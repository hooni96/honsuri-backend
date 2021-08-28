from django.shortcuts import get_object_or_404
from .serializers import *
from recipe.models import * 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RecipeMainView(APIView):
    '''
    recipe main 반환 api
    ___
    파라미터: query로 필터링 내용 전달
        - query에 base로 필터링 내용이 전달될 경우
          : base=1(소주) & base=2(양주) & base=3(맥주) & base=4(와인) & base=5(과일소주)
        - query에 필터링 내용이 없을 경우 : base 전부 포함해서 출력
    결과: 레시피 메인 정보 반환
        - 로그인 되어있을 경우: 북마크 여부 포함해서 반환
        - 로그인 안되어 있을 경우: 북마크 여부 포함 제외
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
        if request.user.is_authenticated: # 로그인 되어 있을 경우
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
    recipe detail 반환 api
    ___
    파라미터: path로 레시피 id 전달
    결과: 레시피 디테일 정보 반환
        - 로그인 되어있을 경우: 북마크 여부 포함해서 반환
        - 로그인 안되어 있을 경우: 북마크 여부 포함 제외
    '''
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            queryset = Recipe.objects.filter(id=pk)

            # 로그인 여부에 따른 북마크 반환 여부
            if request.user.is_authenticated: # 로그인이 되어 있을 경우
                user_id = request.user.pk # 토큰에서 user_id 받아옴
                serializer = RecipeDetailSerializer(queryset, many=True)
                # 북마크 True or False로 반환
                if user_id in serializer.data[0]['bookmark']:
                    serializer.data[0]['bookmark'] = True
                else:
                    serializer.data[0]['bookmark'] = False
            else: # 로그인이 안 되어 있을 경우, 북마크 반환 안 함
                serializer = RecipeDetailSerializerNotLoggedin(queryset, many=True)        
            return Response(serializer.data)
        except:
            return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

class BookmarkView(APIView): 
    def post(self, request, pk):
        '''
        recipe 북마크 생성&삭제 api
            - 북마크가 이미 있으면 삭제, 없으면 생성
        ___
        파라미터: path로 레시피 id 전달
        결과: 북마크 생성 or 삭제 여부
        '''
        try:
            recipe = get_object_or_404(Recipe, pk=pk) # 레시피 객체
            user_id = request.user.pk # 토큰에서 user_id 받아옴
            user = User.objects.get(id = user_id) # user 객체

            if user in recipe.bookmark.all():
                recipe.bookmark.remove(user_id)
                return Response({'message': 'DELETE_BOOKMARK'}, status=status.HTTP_200_OK)
            else:
                recipe.bookmark.add(user_id)
                return Response({'message': 'CREATE_BOOKMARK'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)

        
