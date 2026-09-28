from rest_framework import serializers
from .models import Order
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ['id', 'product', 'user']
        