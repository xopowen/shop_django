from rest_framework import serializers
from shopModul.models import Question

class SerializerQuestion(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields ='__all__'