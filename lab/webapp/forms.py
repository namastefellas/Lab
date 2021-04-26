from django import forms
from django.forms import widgets
from webapp.models import category_choice, Product, Basket, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'leftover', 'product_cost')


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('product_b', 'product_qty')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'phone', 'adress')