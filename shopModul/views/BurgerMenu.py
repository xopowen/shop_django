from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView, Response

from shopModul.models import Catalog
from shopModul.serializers.CatalogSerializers import SerializerCatalogBurgerMneu


class BurgerMenu(APIView):

    """
    url-> "burger-menu/" -> name: BurgerMenu

    get: предостволет каталог отсортированный по полю "order".
         с предосталвением возможности выбрать первичный фильтр.
         кеширует значение на 2 часа.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self,request) -> Response:
        rowCatalogs = Catalog.objects.all().order_by('-order')
        popup_menu = SerializerCatalogBurgerMneu(rowCatalogs, many=True).data
        return Response(status=HTTP_200_OK, data=popup_menu)

