from django.contrib import admin

from shopModul.admin.admin import PropertyValueProduct
from shopModul.models.property.Property import Property
 



@admin.register(Property)
class PropertyAdminModel(admin.ModelAdmin):
    model = Property
    inlines = [PropertyValueProduct]
