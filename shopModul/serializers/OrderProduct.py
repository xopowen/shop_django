

from rest_framework import serializers

from shopModul.models.OrderProduct import OrderProduct
from shopModul.serializers.ProductSerializers import SerializerProductCard


class SerializerOrderProduct(serializers.ModelSerializer):
    product = SerializerProductCard()
    class Meta:
        model = OrderProduct
        fields = '__all__'

class SerializerOrder(serializers.ModelSerializer):
    product = SerializerProductCard()
    class Meta:
        model = OrderProduct
        fields = '__all__'