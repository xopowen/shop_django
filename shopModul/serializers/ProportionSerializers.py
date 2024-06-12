from rest_framework import serializers

from shopModul.models import Proportion


class SerializerProportion(serializers.ModelSerializer):
    class Meta:
        model = Proportion
        fields = '__all__'
