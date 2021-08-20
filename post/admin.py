from django.contrib import admin
from .models import Post  # models.py로부터 Mbti 모델을 가져온다.

admin.site.register(Post)  # Mbti를 관리자 페이지에 등록한다.
