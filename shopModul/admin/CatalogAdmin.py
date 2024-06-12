from django.contrib import admin

from shopModul.admin.admin import PropertyAdmin
from shopModul.models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [PropertyAdmin]

    class Meta:
        model = Catalog
        fields = '__all__'
