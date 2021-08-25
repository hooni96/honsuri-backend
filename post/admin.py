from django.contrib import admin
from .models import Post, PostImage, Comment 

admin.site.register(Post)  # Mbti를 관리자 페이지에 등록한다.
admin.site.register(PostImage)
admin.site.register(Comment)