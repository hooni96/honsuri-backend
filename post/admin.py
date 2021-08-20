from django.contrib import admin
from post.models import Post  # models.py로부터 Mbti 모델을 가져온다.

@admin.register(Post)
class StudioAdmin(admin.ModelAdmin):
  pass