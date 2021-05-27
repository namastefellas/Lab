from django.contrib.auth import authenticate, login, logout
from webapp.models import Basket, Product
from django.shortcuts import render, redirect


def logout_view(request):
    session = request.session.get('basket', [])
    baskets = Basket.objects.filter(pk__in=session)
    if baskets:
        for basket in baskets:
            product = Product.objects.get(pk=basket.product_b.pk)
            product.leftover += basket.product_qty
            product.save()      
    logout(request)
    basket.delete()  
    return redirect('webapp:index')