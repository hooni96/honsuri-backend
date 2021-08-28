from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework import permissions
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view( 
    openapi.Info( 
        title="수리수리혼수리 API", 
        default_version="v1", 
        description="수리수리혼수리 Swagger API 문서", 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('account.urls')),
    path('', include('recipe.urls')), 
    path('', include('music.urls')),
    path('', include('mbti.urls')), 
    path('', include('post.urls')), 
    path('', include('mypage.urls')), 
]

# 디버그=True일때만 swagger 문서가 보이도록 해주는 설정. 
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]
