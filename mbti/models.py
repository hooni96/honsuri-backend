from django.db import models
from core.models import TimestampModel

class Mbti(TimestampModel):
    question = models.TextField(blank=True)
    answer = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = "mbti"