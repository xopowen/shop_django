from rest_framework import serializers

from shopModul.models import Banner
from shopModul.serializers.CatalogSerializers import SerializerCatalog
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink
from shopModul.serializers.ManufacturerSerializers import SerializerManufacturer


class SerializerBanner(serializers.ModelSerializer):
    manufacturer = SerializerManufacturer()
    catalog = SerializerCatalog()

    class Meta:
        model = Banner
        fields = '__all__'
