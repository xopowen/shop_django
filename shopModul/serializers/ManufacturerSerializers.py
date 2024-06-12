from rest_framework import serializers

from shopModul.models.Manufacturer import Manufacturer
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink


class SerializerManufacturer(serializers.ModelSerializer):


    class Meta:
        model = Manufacturer
        fields = '__all__'
