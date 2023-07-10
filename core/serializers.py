from rest_framework import serializers


from .models import Product, Discount, Order, OrderItem, ProductCategory
from authApp.models import User
from authApp.models import Vendor


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "desc"]
        excludes = ["created_at", "updated_at"]

class TempProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id"]
        read_only = True
class ProductSerializer(serializers.ModelSerializer):
    categories = TempProductCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "vendor",
            "quantity",
            "name",
            "desc",
            "sku",
            "price",
            "categories",
        ]
        # depth = 1
        read_only_fields = ["id", "sku"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price", "sub_total"]
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        depth = 1
        model = Order
        fields = ["id", "user", "created_at", "items", "total"]
