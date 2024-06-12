from rest_framework import serializers

from shopModul.models import ImgLink


class SerializerImageLink(serializers.Serializer):
    link = serializers.ImageField()

    class Meta:
        model = ImgLink
        exclude = ['content_type','object_id','content_object']

