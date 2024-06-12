from pprint import pprint

from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Q
from django.urls import resolve

from shopModul.models import Feedback, Catalog, Product, ImgLink, VideoLink, Proportion, Paragraph, ToBook
from shopModul.models.property.Property import Property
from shopModul.models.property.PropertyProduct import PopertyProduct
from shopModul.models.property.PropertyValue import PropertyValue
from shopModul.models.Document import Document

class PropertyProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # product_id = self.instance.product_id
        # """
        # форма показыва разный списко property.
        # если свойсто привязано к продукту будит показаы свойста которые есть у каталога продукат.
        # если нет будутпоказаны свойства укоторых нет категории.
        # """
        # if product_id is None:
        #     self.fields['property'].queryset = self.fields['property'].queryset.filter(catalog_id=None)
        # else:
        #     self.fields['property'].queryset = self.fields['property'].queryset.filter(
        #         Q(catalog_id=Product.objects.get(id=product_id).catalog.pk)
        #                    | Q(catalog_id=None) )




class PropertyAdmin(admin.TabularInline):
    model = Property
    show_change_link = True
    extra = 1


class PropertyProductAdmin(admin.TabularInline):
    form = PropertyProductForm
    model = PopertyProduct
    show_change_link = True
    extra = 1


    def get_parent_object_from_request(self, request):
        """
        Returns the parent object from the request or None.

        Note that this only works for Inlines, because the `parent_model`
        is not available in the regular admin.ModelAdmin as an attribute.
        """
        resolved = resolve(request.path_info)
        if ('object_id' in resolved.kwargs):
            the_parent_object_id = resolved.kwargs['object_id']

            the_object = self.parent_model.objects.get(id=the_parent_object_id)
            return the_object

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'property':

            parent_object: Product = self.get_parent_object_from_request(request)
            if parent_object:
                kwargs["queryset"] = Property.objects.filter(
                Q(catalog_id=parent_object.catalog.pk)
                           | Q(catalog_id=None) )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PropertyValueProduct(admin.TabularInline):
    model = PropertyValue
    extra = 1

class FeedbackInfo(GenericTabularInline):
    model = Feedback
    extra = 1

class ImgGeneric(GenericTabularInline):
    model = ImgLink
    extra = 1
class VideoGeneric(GenericTabularInline):
    model = VideoLink
    extra = 1


class ProportionGeneric(GenericTabularInline):
    model = Proportion
    extra = 1


class DocumentGeneric(GenericTabularInline):
    model = Document
    extra = 1

class ParagraphInline(admin.TabularInline):
    model =  Paragraph
    extra = 1
class ToBookInline(admin.TabularInline):
    model =  ToBook
    extra = 1
    readonly_fields = ['user']