from django.db import models
from core.models import TimestampModel

class Mbti(TimestampModel):
    # 기본적으로, Django에서는 각각의 모델에 id필드를 자동으로 추가해준다
    # 그래서 id 필드는 만들지 않았음
    question = models.TextField(blank=True)
    # 장고에서 3.1 버전부터 JSONField 사용가능
    answer = models.JSONField(default=dict, blank=True)

    # Mbti object 대신에 글 제목이 목록에 나타나게 하기 위해
    def __str__(self):
        return self.question

    class Meta:
        db_table = "mbti"