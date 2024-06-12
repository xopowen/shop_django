from rest_framework import serializers

from shopModul.models import Organization


class SerializerOrganization(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
