from django.db import models

# Create your models here.
from django.db import models

class Recipe(models.Model):
    # 기본적으로, Django에서는 각각의 모델에 id필드를 자동으로 추가해준다
    # 그래서 id 필드는 만들지 않았음
    question = models.TextField(blank=True)
    # 장고에서 3.1 버전부터 JSONField 사용가능
    answer = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = "recipe"

class Bookmark(models.Model):
    # 기본적으로, Django에서는 각각의 모델에 id필드를 자동으로 추가해준다
    # 그래서 id 필드는 만들지 않았음
    question = models.TextField(blank=True)
    # 장고에서 3.1 버전부터 JSONField 사용가능
    answer = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = "bookmark"