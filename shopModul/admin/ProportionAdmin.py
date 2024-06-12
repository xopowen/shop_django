from django.contrib import admin

from shopModul.models import Proportion


@admin.register(Proportion)
class ProportionAdmin(admin.ModelAdmin):
    model = Proportion
