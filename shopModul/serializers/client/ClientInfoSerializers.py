from rest_framework import serializers

from shopModul.models import ClientInfo
from shopModul.serializers.client.UserSerializers import SerializerUser


class SerializerClientInfo(serializers.ModelSerializer):
    user = SerializerUser(required=True)


    class Meta:
        model = ClientInfo
        fields ='__all__'