from django.db.models import Sum
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.utils import json
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import Request,Response
from shopModul.models import Compare, Catalog, Product
from shopModul.serializers.CatalogSerializers import SerializerCatalog, SerializerCatalogCompare
from shopModul.serializers.ProductSerializers import SerializerProductCompare


class CompareViewSet(GenericViewSet):
    """
    permission->IsAuthenticated
    
    get:{
         
        url-> "comparisons/" -> name: compare-catalog-list
        get_catalog_list:
            предостовляет список катологов где есть выбраные товары для сравнения.
                        
        url-> "comparisons/amt/" -> name: get_amt
        get_amt:
            предостовляет коичество товаров для сравнении.
        
        url-> "comparisons/<str:catalog_name>/" -> name: get-compare-by-catalog
        get_compare_by_catalog:
            предостовлет каталог и свойства по которым будут сравниватся товары.
            
        url-> "comparisons/check/<int:product_id>/" -> name: check_product_to_compare
        check_product_to_compare:
            проверет есть ли этот товар(по id) в сравнении у пользователя.
    }
    
    post:{
        url-> "comparisons/add/" -> name: compare-add-product
        add_to_compare:
            добовляет товар в сравнение. 
    }
 
    delete:{
        url-> "comparisons/del/" -> name: del_product_from_compare
        del_product_from_compare:
            удоляет товар из сравнения.
    }
    """
    permission_classes = [IsAuthenticated]

    queryset = Compare.objects
    def get_queryset(self):
        return  Compare.objects.get_or_create(user_id=self.request.user.id)[0]


    def get_catalog_list(self,request:Request)->Response:

        queryset = self.get_queryset()

        products =  queryset.products.all().only('catalog_id')
        catalogs =  Catalog.objects.filter(id__in = products.values('catalog_id'))

        return Response(status=HTTP_200_OK, data=SerializerCatalog(catalogs,many=True).data)


    def get_amt(self,request:Request)->Response:

        amt =  self.get_queryset().products.count()
        return Response(status=HTTP_200_OK, data={'amt':amt})

    def get_compare_by_catalog(self,request:Request,catalog_name:str)->Response:

        catalog = get_object_or_404(Catalog,name =  catalog_name )

        queryset = self.get_queryset().products.filter(catalog__name=catalog_name)

        res_catalog = SerializerCatalogCompare(catalog).data
        products = SerializerProductCompare(queryset,many=True).data

        res = {
            'catalog':res_catalog ,
            'products':products 
        }
        return Response(status=HTTP_200_OK, data= res )

    def add_to_compare(self, request: Request)->Response:
        product = get_object_or_404(Product, id=request.data['product_id'])
        queryset = self.get_queryset()
        queryset.products.add(product)
        queryset.save()

        return Response(status=HTTP_200_OK)

    def check_product_to_compare(self,request:Request,product_id)->Response:

        queryset = self.get_queryset()
        is_product_exist_to_compare = queryset.products.filter(id = product_id ).exists()

        return Response(status= HTTP_200_OK,data={'exists': is_product_exist_to_compare})

    def del_product_from_compare(self,request: Request)->Response:
        product = get_object_or_404(Product, id=request.data['product_id'])
        queryset = self.get_queryset()
        queryset.products.remove(product)
        queryset.save()
        return Response(status=HTTP_200_OK)
