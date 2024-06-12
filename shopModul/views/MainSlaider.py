from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from shopModul.models import Banner
from shopModul.serializers.BannerSerializers import SerializerBanner
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class MainSlider(APIView):
    """
    permission->
    url-> "main-slider/" -> name: main-slider

    get: предостовляет списко Банеров для отображения в слайте отсортированый по полю "order".
        кэш: 2 часа.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self,request)->Response:
        rowBaners = Banner.objects.all().order_by('-order')
        banners = SerializerBanner(instance=rowBaners, many=True ,context={"request": request} ).data  #
        return Response(status=HTTP_200_OK, data=banners)