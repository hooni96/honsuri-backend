from rest_framework import serializers
from mbti.models import Mbti 

class MbtiSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Mbti 
        fields = ['id','question','answer'] 