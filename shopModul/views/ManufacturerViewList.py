from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK
from rest_framework.views import Request ,Response

from shopModul.models import Manufacturer
from shopModul.serializers.ManufacturerSerializers import SerializerManufacturer

from django.utils.decorators import method_decorator

class ManufacturerViewList(viewsets.ViewSet):


    """
    permission->
   
    
    get: {
        url-> "manufactures/" -> name: manufactures-list
        list:
            предостовляет список производитлей.
            кэш: 2 часа.
    }
 
    """
    permission_classes = []
    @method_decorator(cache_page(60*60*2))
    def list(self ,request :Request )->Response:
        rowManufactores = Manufacturer.objects.all()
        manufactures = SerializerManufacturer(rowManufactores, many=True).data
        return Response( status=HTTP_200_OK, data=manufactures)

        