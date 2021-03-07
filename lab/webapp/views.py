from django.shortcuts import render
from webapp.models import Product

# Create your views here.

def index_view(request):
    products = Product.objects.all().order_by('product_name', 'category')
    return render(request, 'index.html', context={'products': products})