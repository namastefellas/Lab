from django.http import response
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Product
from api.serializers.product import ProductSerializer
from django.shortcuts import reverse, get_object_or_404
import json

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serialezer = ProductSerializer(products, many=True)
        response_data = serialezer.data
        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        product_data = request.data
        serializer = ProductSerializer(data=product_data)
        is_valid = serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return JsonResponse({'id': product.id})

class ProductRestView(APIView):
    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('product')
        serializer = ProductSerializer(product)
        response_data = serializer.data
        return Response(response_data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        saved_article = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ProductSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response(status=204)
    
