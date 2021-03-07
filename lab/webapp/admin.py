from django.contrib import admin
from webapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'category', 'leftover', 'product_cost']
    fields = ['id', 'product_name', 'description', 'category', 'leftover', 'product_cost']
    readonly_fields = ['id']

admin.site.register(Product, ProductAdmin)