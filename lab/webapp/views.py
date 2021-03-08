from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from webapp.forms import ProductForm

# Create your views here.

def index_view(request):
    products = Product.objects.all().order_by('product_name', 'category').filter(leftover__gt=1)
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    products = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', context={'product': products})


def create_product(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                product_name=form.cleaned_data['product_name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                leftover=form.cleaned_data['leftover'],
                product_cost=form.cleaned_data['product_cost']
            )
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'product_name': product.product_name,
            'description': product.description,
            'category': product.category,
            'leftover': product.leftover,
            'product_cost': product.product_cost
        })
        return render(request, 'update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product_name = form.cleaned_data['product_name'],
            product.description = form.cleaned_data['description'],
            product.category = form.cleaned_data['category'],
            product.leftover = form.cleaned_data['leftover'],
            product.product_cost = form.cleaned_data['product_cost']
            product.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')