from rest_framework import serializers

from shopModul.models.Basket import Basket
from shopModul.serializers.ProductSerializers import, SerializerProductCard


class SerializerBasket(serializers.ModelSerializer):
    products = SerializerProductCard

    class Meta:
        model = Basket
        fields = '__all__'