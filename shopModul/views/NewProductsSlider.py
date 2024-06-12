from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from shopModul.models import Product
from shopModul.serializers.ProductSerializers import SerializerProductCard


class NewProductSlider(APIView):


    """
    permission->
    url-> "new-products/" -> name: new-products
    
    get: Предостовляет данные о 5 свежый товарах выбраный по подю "date" которое заполняется автоматически.
    
    """
    permission_classes = []
    authentication_classes = []
    @method_decorator(cache_page(60*60*2))
    def get(self,request):
        rowProduct = Product.objects.order_by('date')[:5]
        banners = SerializerProductCard(instance=rowProduct, many=True ,context={"request": request} ).data  #
        return Response(status=HTTP_200_OK, data=banners)