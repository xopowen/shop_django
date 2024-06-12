from rest_framework.serializers import ModelSerializer

from shopModul.models.property.PropertyProduct import PopertyProduct
from shopModul.serializers.property.PropertySerializers import SerializerValue, SerializerProperty

class SerializerPropertyProduct(ModelSerializer):
    value = SerializerValue()
    property = SerializerProperty()
    class Meta:
        model = PopertyProduct
        fields = "__all__"