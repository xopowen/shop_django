from django.db.models import Q
from rest_framework import serializers

from shopModul.models import Product
from shopModul.models.property.PropertyProduct import PopertyProduct
from shopModul.serializers.CatalogSerializers import SerializerCatalog
from shopModul.serializers.DocumentSerializer import SerializerDocument
from shopModul.serializers.FeedbackSerializers import SerializerFeedback, SerializerFeedback_score, \
    SerializerFeedbackOnProduct
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink
from shopModul.serializers.ManufacturerSerializers import SerializerManufacturer
from shopModul.serializers.VideoLinkSerializers import SerializerVideoLink
from shopModul.serializers.ProportionSerializers import SerializerProportion
from shopModul.serializers.property.PropertyProductSerializers import SerializerPropertyProduct


class SerializerProductCompare(serializers.ModelSerializer):
    img = SerializerImageLink(many=True)
    feedback = SerializerFeedback(many=True)
    def to_representation(self, instance):
        row_result = super().to_representation(instance)
        avg_score = [score['score'] for score in row_result.get('feedback')]

        if  len(avg_score) > 0 :
            row_result['avg_score'] = int(sum(avg_score) / len(avg_score))
        else:
            row_result['avg_score'] = 0

        row_property = PopertyProduct.objects.filter((Q(property__catalog_id=instance.catalog.id)
                           | Q(property__catalog_id=None)) & Q(product_id=instance.id) )
        row_result['property'] = SerializerPropertyProduct(row_property,many=True).data
        return row_result

    class Meta:
        model = Product
        fields = '__all__'

class SerializerProductSearch(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'id', 'catalog']


class SerializerProduct(serializers.ModelSerializer):
    img = SerializerImageLink(many=True)
    video = SerializerVideoLink(many=True)
    documents = SerializerDocument(many=True)
    feedback = SerializerFeedback(many=True)
    manufacturer = SerializerManufacturer()
    catalog = SerializerCatalog()
    proportion = SerializerProportion(many=True)
    def to_representation(self, instance):
        row_result = super().to_representation(instance)
        avg_score = [score['score'] for score in row_result.get('feedback')]

        if  len(avg_score) > 0 :
            row_result['avg_score'] = int(sum(avg_score) / len(avg_score))
        else:
            row_result['avg_score'] = 0

        return row_result

    class Meta:
        model = Product
        fields = '__all__'


class SerializerProductCard(serializers.ModelSerializer):
    img = SerializerImageLink(many=True)
    feedback = SerializerFeedback_score(many=True)
    catalog = SerializerCatalog()
    def to_representation(self, instance):
        row_result = super().to_representation(instance)
        avg_score = [score['score'] for score in row_result.get('feedback')]

        if  len(avg_score) > 0 :
            row_result['avg_score'] = int(sum(avg_score) / len(avg_score))
        else:
            row_result['avg_score'] = 0

        return row_result

    class Meta: 
        model = Product
        fields = ['id','name','catalog', 'act', 'price', 'currency', 'feedback', 'img']

class SerializerProductCardOnCatalog(serializers.ModelSerializer):
    img = SerializerImageLink(many=True)
    feedback = SerializerFeedback_score(many=True)

    def to_representation(self, instance):
        row_result = super().to_representation(instance)
        avg_score = [score['score'] for score in row_result.get('feedback')]

        if  len(avg_score) > 0 :
            row_result['avg_score'] = int(sum(avg_score) / len(avg_score))
        else:
            row_result['avg_score'] = 0

        return row_result

    class Meta:
        model = Product
        fields = ['id','name','catalog', 'act', 'price', 'currency', 'feedback', 'img']

class SerializerProductCardOnFeedBack(serializers.ModelSerializer):
    img = SerializerImageLink(many=True)
    feedback = SerializerFeedbackOnProduct(many=True)
    class Meta:
        model = Product
        fields = ['id','name', 'feedback', 'img']