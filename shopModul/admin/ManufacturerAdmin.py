from django.contrib import admin

from shopModul.models import Manufacturer

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer