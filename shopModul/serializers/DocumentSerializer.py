from rest_framework import serializers

from shopModul.models.Document import Document


class SerializerDocument(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
