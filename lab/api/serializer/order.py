from rest_framework import serializers
from webapp.models import Order
from webapp.models import Product
from api.serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product_b = ProductSerializer(many=True, read_only=True)
    class Meta:

        model = Order
        fields = ('user', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at', 'product_b')