from rest_framework import serializers

from shopModul.models.property.PropertyValue import PropertyValue
from shopModul.serializers.property.PropertySerializers import SerializerProperty


class SerializerPropertyValue(serializers.ModelSerializer):
    property = SerializerProperty()


    class Meta:
        model = PropertyValue
        fields = '__all__'

