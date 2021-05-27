from django.urls import include, path
from api.views.products import ProductView, ProductRestView
from api.views.orders import OrderView




app_name = 'api'

product_urls = [
    path('product/', ProductView.as_view(), name='product_list'),
    path('<int:pk>/actions/', ProductRestView.as_view(), name='product_action'),
    path('order/', OrderView.as_view(), name='orders')
]

urlpatterns = [
    path('products', include('product_urls')),
]