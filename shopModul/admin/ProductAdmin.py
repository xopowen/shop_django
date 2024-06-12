from django.contrib import admin

from shopModul.admin.admin import FeedbackInfo, PropertyProductAdmin, ImgGeneric, VideoGeneric, ProportionGeneric, \
    DocumentGeneric
from shopModul.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fieldsets = (("Main info", {'fields': ('name', 'manufacturer', 'catalog','technical_feature')}),
                 ('Accounting info', {'fields': ('amt', 'price', 'old_price', 'currency', 'article', 'act', 'YTP')})
                 , (None, {'fields': ( 'visibility',)}))
    inlines = [DocumentGeneric,ProportionGeneric,ImgGeneric,VideoGeneric,FeedbackInfo]

    def get_inlines(self, request, obj):
        return self.inlines + [PropertyProductAdmin]

