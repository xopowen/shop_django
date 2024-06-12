from rest_framework import serializers

from shopModul.models import Paragraph
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink


class SerializerParagraphs(serializers.ModelSerializer):

    class Meta:
        model = Paragraph
        fields = '__all__'

