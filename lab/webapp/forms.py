from django import forms
from django.forms import widgets
from webapp.models import category_choice

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100, required=True, label='Product Name')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=category_choice, label='Category')
    leftover = forms.IntegerField(min_value=0)
    product_cost = forms.DecimalField(max_digits=7, decimal_places=2, min_value=0.00)