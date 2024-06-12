from rest_framework import serializers
from shopModul.models import Feedback
from shopModul.serializers.client.UserSerializers import SerializerUser

class SerializerFeedbackOnProduct(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'

class SerializerFeedback(serializers.ModelSerializer):
    client = SerializerUser(required=False)
    class Meta:
        model = Feedback
        fields = '__all__'
class SerializerFeedback_score(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['score']
