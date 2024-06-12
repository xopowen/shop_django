from django.contrib import admin

from shopModul.models import ImgLink


@admin.register(ImgLink)
class ImgLinkAdmin(admin.ModelAdmin):
    model = ImgLink