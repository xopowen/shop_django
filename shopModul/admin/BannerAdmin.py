from django.contrib import admin

from shopModul.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    model = Banner