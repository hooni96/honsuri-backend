from django.contrib import admin
from .models import Post, PostImage 

admin.site.register(Post)  # Mbti를 관리자 페이지에 등록한다.
admin.site.register(PostImage)