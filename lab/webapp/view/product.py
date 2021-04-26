from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import ProductForm, SearchForm


# Create your views here.

class IndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('product_name', 'category')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(product_name__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreate(CreateView):
    template_name = 'product/create.html' 
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product/update.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.kwargs.get('pk')})


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:index')