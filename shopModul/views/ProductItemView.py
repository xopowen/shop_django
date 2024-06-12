from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView,Response,Request

from shopModul.models import Product
from shopModul.serializers.ProductSerializers import SerializerProduct


class ProductItemView(APIView):

    """
    permission->
    url-> "catalogs/<str:name>/<int:id_product>/" -> name: product-item-for-id

    get: получает информацию о товаре.
         кэш: 2 часа.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self,request:Request,name,id_product)->Response:
        poduct_item = get_object_or_404(Product,id = id_product, catalog__name = name)

        return Response(status=HTTP_200_OK,
                        data =SerializerProduct(poduct_item,context={'request':request}).data)