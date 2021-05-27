from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductForm, SearchForm, BasketForm, OrderForm
from webapp.models import Product, Basket, Order, ProductOrder
from django.db.models import Q
from django.utils.http import urlencode


class OrderCreate(View):
    def post(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        basket = Basket.objects.filter(pk__in=session)
        form = OrderForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            adress = form.cleaned_data.get("adress")
            phone = form.cleaned_data.get('phone')
            order = Order.objects.create(
                name=name,
                adress=adress,
                phone=phone,
                user=None
            )
            for x in basket:
                qty = x.product_qty
                product = x.product_b
                ProductOrder.objects.create(order=order, product=product)
            basket.delete()
            request.session['basket'] = []

            return redirect('webapp:index')
        else:
            return render(request, 'webapp:basket.html', {'form': form})