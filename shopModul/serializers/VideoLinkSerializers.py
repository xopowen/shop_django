from rest_framework import serializers

from shopModul.models.VideoLink import VideoLink


class SerializerVideoLink(serializers.ModelSerializer):
    class Meta:
        model = VideoLink
        fields = '__all__'