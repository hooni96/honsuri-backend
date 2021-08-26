from django.contrib import admin
from mbti.models import Mbti, MbtiResult  # models.py로부터 Mbti 모델을 가져온다.

admin.site.register(Mbti)  # Mbti를 관리자 페이지에 등록한다.
admin.site.register(MbtiResult)