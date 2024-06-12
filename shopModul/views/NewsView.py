from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK
from rest_framework.views import  Response

from django.shortcuts import get_object_or_404
from shopModul.models import News
from shopModul.serializers.NewsSerializers import SerializerNewsItemFull, SerializerNews
from shopModul.pagination.NewsSetPagination import NewsSetPagination

@cache_page(60*60)
@api_view(['GET'])
def get_news_Item(request, id) -> Response:
    """
    permission->
    url-> news/<int:id>/" -> name: news-Item

    get: предостовляет списко новостей с пагинацией по 3 элемента.
        кэш: 1 час
    """

    rowNewsItem = get_object_or_404(News, id=id)
    newsItem = SerializerNewsItemFull(rowNewsItem).data
    return Response(status=HTTP_200_OK, data=newsItem)



class NewsView(ListAPIView):

    """
    permission->
    url-> "news/" -> name: new-news
    
    get: предостовляет списко новостей с пагинацией по 3 элемента.
        кэш: 1 час
    """
    queryset = News.objects.all().order_by('date')
    serializer_class = SerializerNews
    pagination_class = NewsSetPagination
    renderer_classes = [JSONRenderer]
    @method_decorator(cache_page(60*60))
    def get(self,*args,**kwargs):
        return super().get(*args,**kwargs)
