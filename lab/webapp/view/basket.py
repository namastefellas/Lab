from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Basket
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import BasketForm, SearchForm, Product


class BasketCreate(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.leftover > 0:
            try:
                basket = Basket.objects.get(product_b__pk=product.pk)
                basket.product_qty += 1
                basket.product_qty = product.leftover
                basket.save()

            except Basket.DoesNotExist:
                Basket.objects.create(
                    product_b=product,
                    product_qty=1
                )
            product.leftover -= 1
            product.save()
            
        return redirect('index')



class BasketView(ListView):
    template_name = 'basket/basket.html'
    model = Basket
    context_object_name = 'baskets'

    def get_context_data(self, **kwargs):
        total_stuff = []
        total = 0
        basket = Basket.objects.all()
        for i in basket:
            total += i.product_b.product_cost * i.product_qty
            total_stuff.append({'total_stuff': i, 'total': i.product_qty * i.product_b.product_cost })
        context = super().get_context_data(**kwargs)
        context['total_stuff'] = total_stuff
        context['total'] = total
        return context




class BasketDelete(DeleteView):
    model = Basket

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('basket_list')