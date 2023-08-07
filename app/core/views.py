from django.shortcuts import render, get_object_or_404
from rest_framework import generics, pagination, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from typing import List
from authApp.models import Vendor, User
from .models import Product, ProductCategory, Order, OrderItem
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    RefundOrderSerializer,
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

class RefundOrderView(generics.CreateAPIView):
    """Takes the two set of parameters: Order and Complaint
    
    Keyword arguments:
    order -- id of the order to be refunded
    complaint -- reason for the refund (compulsory)
    Return: status code 200
    """
    
    queryset = Order.objects.all()
    serializer_class = RefundOrderSerializer

    def perform_create(self, serializer):
        # Ensure that the user can only log a refund request for their own orders
        user = self.request.user
        order_id = self.request.data.get('order_id') 

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            # Handle case when the order_id does not exist
            raise ValidationError("Invalid Order ID")

        if order.user != user:
            raise ValidationError("You can only log a refund request for your own orders.")

        serializer.save(user=user)
        