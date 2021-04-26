from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Basket
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import BasketForm, SearchForm, Product, OrderForm


class BasketCreate(View):
    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.leftover > 0:
            try:
                basket = Basket.objects.get(product_b__pk=product.pk, pk__in=session)
                basket.product_qty += 1
                basket.save()

            except Basket.DoesNotExist:
                basket = Basket.objects.create(
                    product_b=product,
                    product_qty=1
                )
                session.append(basket.id)
                product.leftover -= 1
                product.save()

            
            request.session['basket'] = session
            return redirect('webapp:index')




class BasketView(ListView):
    template_name = 'basket/basket.html'
    model = Basket
    context_object_name = 'baskets'
    form = OrderForm

    sessions = None

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket',[])
        self.sessions = session
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        total_stuff = []
        total = 0
        basket = Basket.objects.all()
        for i in self.sessions:
            i = Basket.objects.all().get(id=i)
            total += i.product_b.product_cost * i.product_qty
            print(total)
            total_stuff.append({'total_stuff': i, 'total': i.product_qty * i.product_b.leftover})
            print(total_stuff)
        context = super().get_context_data(**kwargs)
        context['total_stuff'] = total_stuff
        context['total'] = total
        context['form'] = self.form
        return context




class BasketDelete(DeleteView):
    model = Basket

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        if self.get_object().pk in session:
            session.remove(self.get_object().pk)
            request.session['basket'] = session
        return self.delete(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('webapp:basket_list')