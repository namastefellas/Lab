"""lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.view.product import IndexView, ProductView, ProductCreate, ProductUpdate, ProductDelete
from webapp.view.basket import BasketCreate, BasketView, BasketDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('product/create/', ProductCreate.as_view(), name='add_product'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('basket/<int:pk>/', BasketCreate.as_view(), name='basket'),
    path('basket/list', BasketView.as_view(), name='basket_list'),
    path('product/delete/<int:pk>', BasketDelete.as_view(), name='basket_delete')
]
