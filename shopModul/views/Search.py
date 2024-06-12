from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from shopModul.models import Product, Catalog
from shopModul.serializers.CatalogSerializers import SerializerCatalogSearch
from shopModul.serializers.ProductSerializers import SerializerProductSearch


class Search(APIView):


    """
    permission->
    url-> "search/<str:string_search>/" -> name: search
    
    get: предостовялет информацию для показа в подсказке под полем ввода.
        информация о найтеный товарах.(краткое.)
        ифнормацию о найтеный каталогах .(краткое.)
    """
    authentication_classes = []
    permission_classes = []
    def get(self,request:Request,string_search)->Response:
        raw_product = Product.objects.filter(name__icontains=string_search).only('name','id','catalog')
        raw_catalog = Catalog.objects.filter(name__icontains=string_search).only('name','id')
        products = SerializerProductSearch(raw_product,many=True)
        catalogs = SerializerCatalogSearch(raw_catalog,many=True)
        result = {
            'products': products.data,
            'categories':catalogs.data,
        }
        return Response(status=HTTP_200_OK, data=result)


