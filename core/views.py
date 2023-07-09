from django.shortcuts import render
from rest_framework import generics, pagination
from typing import List
from authApp.models import Vendor
from .models import Product, ProductCategory, Cart, Order, OrderItem
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    CartSerializer,
    OrderSerializer,
    OrderItemSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        vendor = self.request.user
        quantity = self.request.data.get("quantity")
        name = self.request.data.get("name")
        desc = self.request.data.get("desc")
        price = self.request.data.get("price")
        category_list = self.request.data.get("categories")
        print(category_list)

        categories = []
        for category in category_list:
            product_category = ProductCategory.objects.get(id=category)
            categories.append(product_category)

        product = Product(
            vendor=vendor,
            quantity=quantity,
            name=name,
            desc=desc,
            price=price,
            categories=categories,
        )
        
        product.save()
        
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class CartListView(generics.ListCreateAPIView):
    queryset = Cart.objects.filter(order__isnull=True)
    serializer_class = CartSerializer

    def calculate_cart_total(cart_items):
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.get_total_price()
        return total_price


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user, order__isnull=True)

        order = serializer.save(user=user)
        order_items = []

        for cart_item in cart_items:
            order_item = OrderItem(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price * cart_item.quantity,
            )
            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)
        cart_items.delete()


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        user = self.request.user
        product_id = self.request.data.get("product_id")
        quantity = self.request.data.get("quantity")

        product = Product.objects.get(id=product_id)
        cart = Cart(user=user, product=product, quantity=quantity)
        cart.save()


class CartUpdateView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartRetrieveView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDeleteView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
