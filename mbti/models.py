from django.db import models
from core.models import TimestampModel
from recipe.models import Recipe # 칵테일 이름, 사진파일명, 칵테일 아이디


class Mbti(TimestampModel):
    question = models.TextField(blank=True)
    answer = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = "mbti"


class MbtiResult(TimestampModel):
    mbti = models.CharField(max_length=10, verbose_name="mbti 유형", unique=True)
    comment = models.TextField(blank=True)
    recipe = models.OneToOneField(Recipe,on_delete=models.CASCADE)

    def __str__(self):
        return self.mbti

    class Meta:
        db_table = "mbti_result"