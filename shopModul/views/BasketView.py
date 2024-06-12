from django.db.models import F
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

from shopModul.models.Basket import Basket
from shopModul.models.OrderProduct import OrderProduct
from shopModul.serializers.OrderProduct import SerializerOrderProduct
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
class BasketView(GenericAPIView):
    """
    permission->IsAuthenticated
    url-> "basket/" -> name: basket
    
    get: предостволет довары у пользователя в карзине.
         Находит корзину пользователя и перёт все не оформленные заказы. 

    
    post: Получает или создаёт карзину пользователя. Создает заказ на полученынй товар. 
          Если подобный заказ есть то увеличиват количество товара в заказе. 
    
    delete: удаляет заказ из корзины.
    """
    permission_classes = [IsAuthenticated]

    def get(self,request)->Response:
        raw_products =  get_object_or_404(Basket,user_id=request.user.pk).order_product.all()
        products = SerializerOrderProduct(raw_products.filter(issued=False),many=True).data
        return Response(status = HTTP_200_OK,data= products)
    def post(self,request):

        basket = Basket.objects.get_or_create(user_id=request.user.pk)

        if product_id := request.data.get('product_id',None):
            order_product,isCreate = OrderProduct.objects.get_or_create(product_id=product_id,issued=False)
            if(isCreate):
                basket[0].order_product.add(order_product )
            else:
                order_product.amt =F('amt') + 1
                order_product.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


    def delete(self,request):
        get_object_or_404( Basket,user_id=request.user.pk )
        if product_id := request.data.get('product_id',None):
            order_product = get_object_or_404(OrderProduct,product_id=product_id,issued=False)
            order_product.delete()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
