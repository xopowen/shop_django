from rest_framework import serializers

from shopModul.models import Event
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink


class SerializerEvent(serializers.ModelSerializer):
    img = SerializerImageLink(many = True)
    class Meta:
        model = Event
        fields ="__all__"