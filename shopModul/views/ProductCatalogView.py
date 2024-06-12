from django.db.models import Q
from django.http import QueryDict
from rest_framework.request import Request
from rest_framework.views import APIView

from shopModul.models import Product
from shopModul.models.property.PropertyProduct import PopertyProduct
from shopModul.pagination.ProductCatalogSetPagination import ProductCatalogSetPagination
from shopModul.serializers.ProductSerializers import SerializerProductCardOnCatalog


class ProductCatalogView(APIView, ProductCatalogSetPagination):

    """
    permission->
    url-> "catalogs/<str:name>/" -> name:catalog-product
    url-> "manufactures/<str:name>/" -> name: manufacture-product
    get: отфильтровывает товары с учётом фильтров из request.query_params.
    """

    @staticmethod
    def get_custom_filter(q_dict: QueryDict) -> list[Q]:
        # создаёт фильтр нв основе тела ajax запроса
        listQ = []
        q_listTuple = q_dict.lists()
        for filterTuple in q_listTuple:
            name, value = filterTuple
            if name in ['order', 'price__lte', 'price__gte', 'page']:
                continue
            listQ.append(Q(property__name__in=[name]))
            listQ.append(Q(value__value__in=value))
        return listQ

    def get(self, request: Request, name, **kwargs):
        if kwargs.get('is_manufacture',None):
            raw_Products = Product.objects.filter(Q(manufacturer__name=name))
        else:
            raw_Products = Product.objects.filter(Q(catalog__name=name))

        filter_request = request.query_params
        order = filter_request.get('order', "date")

        min_price = filter_request.get('price__lte', None)
        if (min_price is not None and min_price != ''):
            raw_Products = raw_Products.filter(Q(price__lte=float(min_price)))

        max_price = filter_request.get('price__gte', None)
        if max_price is not None and max_price != '':
            raw_Products = raw_Products.filter(Q(price__gte=float(max_price)))

        filter_query = self.get_custom_filter(filter_request)
        if (len(filter_query) > 0):
            poperty_product = PopertyProduct.objects.filter(*filter_query).only('product__id')
            raw_Products = raw_Products.filter(id__in=poperty_product)

        pagination_result = self.paginate_queryset(raw_Products.order_by(order), request, self)
        serialized_products = SerializerProductCardOnCatalog(pagination_result, many=True)
        return self.get_paginated_response(serialized_products.data)
