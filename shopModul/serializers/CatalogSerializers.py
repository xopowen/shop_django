from django.db.models import Q
from rest_framework import serializers

from shopModul.models import Catalog
from shopModul.models.property.Property import Property
from shopModul.models.property.PropertyValue import PropertyValue
from shopModul.serializers.property.PropertySerializers import SerializerProperty
from shopModul.serializers.property.PropertyValueSerializers import SerializerPropertyValue

class SerializerCatalogCompare(serializers.ModelSerializer):

    def to_representation(self, instance):
        res = super().to_representation(instance)
        property = Property.objects.filter(Q(catalog_id=instance.pk)
                                         | Q(catalog_id=None))
        res['property'] = SerializerProperty(property,many=True).data
        return res

    class Meta:
        model = Catalog
        fields = '__all__'

class SerializerCatalogSearch(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['name','id']

class SerializerCatalog(serializers.ModelSerializer):


    class Meta:
        model = Catalog
        fields = '__all__'


class SerializerCatalogBurgerMneu(serializers.ModelSerializer):

    def to_representation(self, instance):
        rowData  =  super().to_representation(instance)

        rowData['choices'] = SerializerPropertyValue(PropertyValue.objects.filter(property__catalog=instance.id,
                                                                                  show_menu=True),
                                                     many=True ).data

        return rowData

    class Meta:
        model = Catalog
        fields = ['id', 'name','order']