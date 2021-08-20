"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# drf-yasg --------------------
from django.conf.urls import url
from rest_framework import permissions
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# -----------------------------
# from mbti.views import helloworld  # views.py에서 우리가 만든 helloworld 함수를 가져온다.

# drf-yasg --------------------
schema_view = get_schema_view( 
    openapi.Info( 
        title="수리수리혼수리 API", 
        default_version="v1", 
        description="수리수리혼수리 Swagger API 문서", 
        # terms_of_service="https://www.google.com/policies/terms/", 
        # contact=openapi.Contact(name="김다인", email="dainlinda@gmail.com"), 
        # license=openapi.License(name="Test License"), 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    path('', include('mbti.urls')), # mbti/urls.py 사용
    path('', include('post.urls')), # opost/urls.py 사용
]

# 이건 디버그일때만 swagger 문서가 보이도록 해주는 설정. 
# URLPATH도 이 안에 설정 가능해서, debug일때만 작동시킬 api도 설정할 수 있음.
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]
