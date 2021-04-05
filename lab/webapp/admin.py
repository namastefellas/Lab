from django.contrib import admin
from webapp.models import Product, Basket, Order

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'category', 'leftover', 'product_cost']
    fields = ['id', 'product_name', 'description', 'category', 'leftover', 'product_cost']
    readonly_fields = ['id']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_b', 'product_qty']
    fields = ['product_b', 'product_qty']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'adress', 'created_at']
    fields = ['name', 'phone', 'adress']

admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)