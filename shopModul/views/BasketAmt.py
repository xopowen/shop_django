from django.db.models import Sum
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView, Response, Request

from shopModul.models.Basket import Basket


class BasketAmt(APIView):
    '''
    permission->IsAuthenticated
    url-> "basket/amt/" -> name:basket-amt
    get -> Response.data = {'amt':int}
    предостволет данные о количтетве доваров у пользователя в карзине.
    Находит корзину пользователя и перёт все не оформленные заказы арикируя  их по полю "amt"
 
    '''
    permission_classes = [IsAuthenticated]


    def get(self,request:Request)-> Response:

        basket = get_object_or_404(Basket,user=request.user)

        amt =  basket.order_product.filter(issued=False).aggregate(amt = Sum('amt'))

        return Response(status = HTTP_200_OK,data= amt )
