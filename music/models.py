from django.db import models
from core.models import TimestampModel

class Music(TimestampModel):
    title = models.CharField(max_length=100, verbose_name="노래 제목")
    photo = models.CharField(max_length=100, verbose_name="앨범 사진 이름")
    singer = models.CharField(max_length=100, verbose_name="가수 이름")
    file_name = models.CharField(max_length=100, verbose_name="음원 파일 이름")

    class Meta:
        db_table = "music"
    
    def __str__(self):
        return self.title
