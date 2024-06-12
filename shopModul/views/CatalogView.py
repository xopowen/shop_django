from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from shopModul.models import Catalog
from shopModul.serializers.CatalogSerializers import SerializerCatalog
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
class CatalogView(APIView):
    """
        url-> "catalogs/" -> name:catalogs

        get: возврожает лист каталогов.
            кэш: 2 часа.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self,request)->Response:
        raw_Catalogs = Catalog.objects.all()
        catalog = SerializerCatalog(raw_Catalogs, many=True,context={'request': request} ).data

        return Response(status=HTTP_200_OK, data=catalog)


