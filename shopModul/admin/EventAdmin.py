from django.contrib import admin

from shopModul.admin.admin import ImgGeneric, ToBookInline
from shopModul.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    inlines = [ToBookInline,ImgGeneric]