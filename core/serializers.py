from rest_framework import serializers

from .models import Product, Discount, Order, OrderItem, ProductCategory
from authApp.models import User
from vendor.models import Vendor


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'desc']
        #excludes = ['created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'sku', 'price', 'categories']
        #depth = 1
        read_only_fields = ['id', 'sku']

        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','items', 'user', 'total']
        depth = 1
        
class unknown():
    pass  
'''  
    name = serializers.CharField()
    desc = serializers.TextField()
    sku = serializers.CharField(max_length=200, unique=True)
    price = serializers.DecimalField()
    categories = serializers.ManyRelatedField() 
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Product(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.sku = instance.sku 
        instance.price = validated_data.get('price', instance.price)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.updated_at = serializers.DateTimeField(auto_now=True)
        
        instance.save()
        return instance
'''
        
        
class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        
