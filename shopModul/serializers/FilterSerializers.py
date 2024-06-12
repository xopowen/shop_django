
from rest_framework import serializers

from shopModul.models import Filter
from shopModul.models.Choice import Choice
from shopModul.serializers.ChoiceSerializers import SerializerChoice


class SerializerFilter(serializers.ModelSerializer):
    def to_representation(self, instance):
        rowData  =  super().to_representation(instance)
        choices = Choice.objects.all().filter(catalog_id=rowData['catalog'],filter_id=rowData['id'])
        rowData['choices'] = SerializerChoice(choices,many=True).data
        return rowData
    class Meta:
        model = Filter
        fields = '__all__'