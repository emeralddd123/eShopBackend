from django.shortcuts import render
from rest_framework import generics, pagination

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = pagination.LimitOffsetPagination
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.LimitOffsetPagination
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    