from django.shortcuts import render, get_object_or_404
from rest_framework import generics, pagination, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from typing import List
from authApp.models import Vendor, User
from .models import Product, ProductCategory, Order, OrderItem
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    OrderSerializer,
    OrderItemSerializer,
)
from django.forms.models import model_to_dict


class CategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class CategoryCreateView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (
        []
    )  # Only Admins or moderator should be allowed to create category


class ProductListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        vendor_id = self.request.user.id
        quantity = self.request.data.get("quantity")
        name = self.request.data.get("name")
        desc = self.request.data.get("desc")
        price = self.request.data.get("price")
        category_list = self.request.data.get("categories")
        print(category_list)
        print(vendor_id)
        vendor = User.objects.get(id=vendor_id)
        categories = []
        for category in category_list:
            product_category = ProductCategory.objects.get(id=category["id"])
            categories.append(product_category)

        product = Product(
            vendor=vendor,
            quantity=quantity,
            name=name,
            desc=desc,
            price=price,
        )
        product.save()
        product.categories.set(categories)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
