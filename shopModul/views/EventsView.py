from rest_framework.generics import ListAPIView
from shopModul.models.Event import Event
from shopModul.serializers.EventSerializers import SerializerEvent

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class EventsView(ListAPIView):

    """
    permission->
    url-> "about-company/" -> name: events-list
    
    get: предостовляет список мероприятий.
        кэш: 2 часы
    """
    queryset = Event.objects.all()
    serializer_class = SerializerEvent

    @method_decorator(cache_page(60*60*2))
    def get(self,*args,**kwargs):
        return super().get(self,*args,**kwargs)
