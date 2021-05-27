from django.contrib import admin
from django.urls import path
from webapp.view.product import IndexView, ProductView, ProductCreate, ProductUpdate, ProductDelete
from webapp.view.basket import BasketCreate, BasketView, BasketDelete
from webapp.view.order import OrderCreate

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('product/create/', ProductCreate.as_view(), name='add_product'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('basket/<int:pk>/', BasketCreate.as_view(), name='basket'),
    path('basket/list', BasketView.as_view(), name='basket_list'),
    path('basket/delete/product/<int:pk>', BasketDelete.as_view(), name='basket_delete'),
    path('order/create', OrderCreate.as_view(), name='create_order')
]