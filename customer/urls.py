from django.urls import path
from .views import *

urlpatterns = [
    path('index/',indexview.as_view(),name='index'),
    path('details/<int:id>',detailview.as_view(),name='details'),
    path('cartadd/<int:id>',addtocart,name='cartadd'),
    path('cartview/',CartView.as_view(),name='cartview'),
    path('order/<int:id>',CheckoutView.as_view(),name='order'),
    path('cartview/<int:id>',RemoveCartItem,name='cartdel'),
    path('ordersListview/',OrdersListView.as_view(),name='orderlist'),
    path('orderdel/<int:id>',CancelOrder,name='orddel'),
]
