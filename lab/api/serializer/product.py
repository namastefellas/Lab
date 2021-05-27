from rest_framework import serializers
from webapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'description', 'category', 'leftover', 'product_cost')
        read_only_fields =  ('id',)
