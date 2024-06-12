from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response

from shopModul.models import ClientInfo
from shopModul.serializers.client.ClientInfoSerializers import SerializerClientInfo
from shopModul.serializers.client.UserSerializers import SerializerUser


class ClientInfoView(RetrieveAPIView):
    """
    url-> "client-info/" -> name: client-info
    put: изменяет или создаёт информацию в профиле пользоватля необходимую для совершения покупки.
    """
    permission_classes = [IsAuthenticated]
    queryset = ClientInfo.objects
    serializer_class = SerializerClientInfo
    def get_object(self):
       return self.get_queryset().get_or_create(user_id = self.request.user.id)[0]

    def put(self,request):
        user = request.user
        serializer_user = SerializerUser(user, data=request.data, partial=True)
        serializer_user.is_valid(raise_exception=True)
        serializer_user.save()

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)





