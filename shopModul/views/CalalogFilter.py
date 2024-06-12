from django.db.models import Q
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView, Response

from shopModul.models.property.Property import Property
from shopModul.serializers.property.PropertySerializers import SerializerPropertyWithValue
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class CatalogFilter(APIView):
    """
        url-> "filter/<str:name>/ -> name: catalog-filter
        get: Возврощает данные для фильтра по названию каталога.
             берёт свойства у которых есть привяска к выбрному каталогу и у которыйх "catalog__name" = None.
             кэш: 2 часа.

    """
    @method_decorator(cache_page(60*60*2))
    def get(self,request,name)->Response:
        raw_property_catalog = Property.objects.filter(Q(catalog__name = name) )
        raw_property_catalog2 = Property.objects.filter(Q(catalog__name = None) )
        result = SerializerPropertyWithValue(raw_property_catalog.union(raw_property_catalog2), many=True).data
        return Response(status= HTTP_200_OK, data=result)