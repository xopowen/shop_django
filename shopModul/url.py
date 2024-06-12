from django.conf.urls.static import static
from django.urls import path
from shop_django import settings
from shop_django.views import index
from .views.BasketAmt import BasketAmt
from .views.BasketView import BasketView
from .views.BurgerMenu import BurgerMenu
from .views.CalalogFilter import CatalogFilter
from .views.CatalogView import CatalogView
from .views.ClientInfoView import ClientInfoView
from .views.CompareView import CompareViewSet
from .views.EventsView import EventsView
from .views.MainSlaider import MainSlider
from .views.ManufacturerViewList import ManufacturerViewList
from .views.NewProductsSlider import NewProductSlider
from .views.NewsView import get_news_Item, NewsView
from .views.OrderViews import OrderProductAmtCouner, OrderProductView
from .views.ProductCatalogView import ProductCatalogView
from .views.ProductItemView import ProductItemView
from .views.QuestionView import QuestionView
from .views.Search import Search
from .views.ToBookView import ToBookView
from .views.views import set_csrf_token
from .views.FeedBackProductView import FeedBackProductView
app_name = 'shopModul'



urlpatterns = [
    path('csrf-token/',set_csrf_token, name='csrf-token'),
    path('burger-menu/',BurgerMenu.as_view(),name='BurgerMenu'),
    path('search/<str:string_search>/', Search.as_view(), name='search'),
    path('main-slider/',MainSlider.as_view(), name='main-slider'),

    path('product/<int:product_id>/feedback/add/',
         FeedBackProductView.as_view({'post':'post_create'}),name= "add-feedback-product"),

    path("catalogs/",CatalogView.as_view(),name='catalogs'),
    path("catalogs/<str:name>/", ProductCatalogView.as_view(), name='catalog-product'),
    path('filter/<str:name>/',CatalogFilter.as_view(),name = 'catalog-filter'),

    path('catalogs/<str:name>/<int:id_product>/',ProductItemView.as_view(),name = 'product-item-for-id'),

    path('manufactures/',
         ManufacturerViewList.as_view({'get': 'list'}),
         name='manufactures-list'),
    path('manufactures/<str:name>/', ProductCatalogView.as_view(),kwargs={'is_manufacture': True},name='manufacture-product'),

    path("news/<int:id>/", get_news_Item, name='news-Item'),
    path("news/", NewsView.as_view(), name='new-news'),
    path('about-company/', EventsView.as_view(), name='events-list'),
    path('to-book/',ToBookView.as_view(), name='to-book'),

    path("basket/", BasketView.as_view(), name='basket'),
    path("basket/amt/", BasketAmt.as_view(), name='basket-amt'),
    path('basket/order/<int:order_id>/add-amt/',
         OrderProductAmtCouner.as_view({'post':'add'}),
         name='order-add-amt'),
    path('basket/order/<int:order_id>/mines-amt/',
         OrderProductAmtCouner.as_view({'post':'mines'}),
         name='order-mines-amt'),
    path('basket/order/formalization/',
         OrderProductView.as_view(),
         name='order-formalization'),

    path('client-info/',ClientInfoView.as_view(),name='client-info' ),
    path('client-info/orders/', OrderProductView.as_view(), name='orders-product'),
    path('client-info/feed-backs/',
         FeedBackProductView.as_view({'get':'get_list'}),
         name='feedbacks-product'),

    path('comparisons/',
         CompareViewSet.as_view({'get': 'get_catalog_list'}),
         name='compare-catalog-list'),
    path('comparisons/amt/',
         CompareViewSet.as_view({'get':'get_amt'}),
         name='compare-get-amt'),
    path('comparisons/add/',
         CompareViewSet.as_view({'post':'add_to_compare'}),
         name='compare-add-product'),
    path('comparisons/check/<int:product_id>/',
         CompareViewSet.as_view({'get': 'check_product_to_compare'}),
         name='check-product-to-compare'),
    path('comparisons/del/',
         CompareViewSet.as_view({'delete':'del_product_from_compare'}),
         name='del-product-from-compare'),
    path('comparisons/<str:catalog_name>/',
         CompareViewSet.as_view({'get': 'get_compare_by_catalog'}),
         name='get-compare-by-catalog'),

    path("ask-question/",QuestionView.as_view(),name='ask-question'),
    path("new-products/",NewProductSlider.as_view(),name='new-products'),

]
