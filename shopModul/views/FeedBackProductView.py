from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import Response, Request
from rest_framework.viewsets import GenericViewSet

from shopModul.models import Product
from shopModul.serializers.FeedbackSerializers import SerializerFeedbackOnProduct, SerializerFeedback
from shopModul.serializers.ProductSerializers import SerializerProductCardOnFeedBack


class FeedBackProductView(GenericViewSet):

    """
    permission->IsAuthenticated
    get: {
        url-> "client-info/feed-backs/" -> name: feedbacks-product
        get_list:
            предостовляет отзевы которые оставил пользователь у продуктов.
    }
    post:{
        url-> "product/<int:product_id>/feedback/add/" -> name: add-feedback-product
        post_create:
            создаёт коментарий к продукту.
    }
    """
    permission_classes = [IsAuthenticated]
    queryset = Product.objects
    serializer_class = SerializerProductCardOnFeedBack


    def get_queryset(self):
        return Product.objects.filter(feedback__client_id = self.request.user.id)

    def get_list(self,request:Request)->Response:
        data = self.get_serializer(self.get_queryset(),many=True).data
        return Response(data = data)

    def post_create(self,request:Request,product_id)->Response:
        serializer_data = SerializerFeedback(data=request.data  )
        product = get_object_or_404(Product,id = product_id)
        if serializer_data.is_valid():
            serializer_data.save( client=request.user,content_object=product)
            return Response(data = serializer_data.data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST,data=serializer_data.errors)



