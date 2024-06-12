from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

from shopModul.models.ToBook import ToBook


class ToBookView(APIView):

    """
    permission->
    url-> "'to-book/" -> name: to-book
 
    post: оставить заявку на участие в мероприятии
    """
    permission_classes = [IsAuthenticated]
    def post(self, request)->Response:
        user = request.user
        event_id = request.data.get('event_id',None)
        if(event_id is not None):
            obj,isCreate = ToBook.objects.get_or_create(user_id=user.pk,event_id=event_id)
            if isCreate:
                return Response(status= HTTP_200_OK)
            else:
                return Response(status= HTTP_400_BAD_REQUEST,data= {'error':'Заявление уже отправлено.'})
        return Response(status=HTTP_400_BAD_REQUEST)