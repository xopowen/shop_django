from django.db.models import F
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet, ViewSetMixin
from rest_framework.views import Request, Response

from shopModul.models import OrderProduct
from shopModul.models import Basket
from shopModul.serializers.OrderProduct import SerializerOrder


class OrderProductView(GenericAPIView):

    """
    permission-> IsAuthenticated
    
    url-> "client-info/orders/" -> name: orders-product
    get: предостовляет информацию о оформленый товарах.
    
    url-> "basket/order/formalization/" -> name: order-formalization
    put: изменяет статус заказа на оформленный. 
 
    """
    queryset = OrderProduct.objects
    serializer_class = SerializerOrder
    permission_classes = [IsAuthenticated]
    def put(self,request):
        orders_id_list:list = self.request.data['orders']
        orders = OrderProduct.objects.filter(id__in = orders_id_list)
        print(orders_id_list,orders)
        for order in orders:
            order.issued = True
            order.save()

        return Response(status=HTTP_200_OK)

    def get(self,request):
        raw_products = get_object_or_404(Basket, user_id=request.user.pk).order_product.all()

        return Response(self.get_serializer(raw_products.filter(issued=True), many=True).data)




class OrderProductAmtCouner(ViewSet, ViewSetMixin):
    """
    permission->
   
    post:{
        url-> "'basket/order/<int:order_id>/add-amt/" -> name: order-add-amt
        add: добовляет товар в заказе (количество товарва возростает на 1) 
        
        url-> "basket/order/<int:order_id>/mines-amt/" -> name: order-mines-amt
        mines: отнемает товар в заказе (количество товарва уменьшается на 1) 
    }
    """
    permission_classes = [IsAuthenticated]
    def add(self,request:Request,order_id:int,*args, **kwargs)->Response:
        order = get_object_or_404(OrderProduct,id = order_id)
        order.amt = F('amt') + 1
        order.save()
        return Response(status= HTTP_200_OK)

    def mines(self,request:Request,order_id:int)->Response:
        order = get_object_or_404(OrderProduct, id = order_id)
        order.amt = F('amt') - 1
        order.save()
        return Response(status= HTTP_200_OK)