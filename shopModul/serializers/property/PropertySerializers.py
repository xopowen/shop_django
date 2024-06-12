from rest_framework import serializers

from shopModul.models import Property
from shopModul.models.property.PropertyValue import PropertyValue


class SerializerProperty(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'

class SerializerValue(serializers.ModelSerializer):
    class Meta:
        model = PropertyValue
        fields = '__all__'
class SerializerPropertyWithValue(serializers.ModelSerializer):


    def to_representation(self, instance):
        raw_data  =  super().to_representation(instance)

        raw_data['choices'] = SerializerValue(PropertyValue.objects.filter(property_id=instance.id,
                                                                          show_filter=True),
                                                many=True ).data
        return raw_data

    class Meta:
        model = Property
        fields = '__all__'