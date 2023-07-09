from rest_framework import serializers

from .models import Product, Discount, Order, OrderItem, ProductCategory, Cart
from authApp.models import User
from authApp.models import Vendor


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'desc']
        excludes = ['created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','vendor', 'quantity', 'name', 'desc', 'sku', 'price', 'categories']
        depth = 1
        read_only_fields = ['id', 'sku']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price', 'subtotal']
        depth = 1
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        depth=1
        model = Order
        fields = ['id', 'user', 'created_at', 'items','total']
        
        
        
class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.get_total_price()

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1