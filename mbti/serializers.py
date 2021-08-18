from rest_framework import serializers # serializer import
from mbti.models import Mbti # 선언한 모델 import
from drf_yasg import openapi

# class EmailMessageField(serializers.JSONField):
#     class Meta:
#         swagger_schema_fields = {
#             "type": openapi.TYPE_OBJECT,
#             "title": "Email",
#             "properties": {
#                 "subject": openapi.Schema(
#                     title="Email subject",
#                     type=openapi.TYPE_STRING,
#                 ),
#                 "body": openapi.Schema(
#                     title="Email body",
#                     type=openapi.TYPE_STRING,
#                 ),
#             },
#             "required": ["subject", "body"],
#          }

# ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있음
class MbtiSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Mbti  # 모델 설정
        fields = '__all__'  # 필드 설정
    # message = EmailMessageField()