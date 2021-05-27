from django.http import response
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Order
from api.serializers.product import OrderSerializer
from django.shortcuts import reverse, get_object_or_404
import json

class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serialezer = OrderSerializer(orders, many=True)
        response_data = serialezer.data
        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        order_data = request.data
        serializer = OrderSerializer(data=order_data)
        is_valid = serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return JsonResponse({'id': order.id})

    

