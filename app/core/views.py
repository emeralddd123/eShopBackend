from rest_framework import generics, pagination
from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import ValidationError
from .models import ProductCategory, Order, Refund
from .serializers import (
    ProductCategorySerializer,
    RefundOrderSerializer,
)
from authApp.permissions import IsCustomerOrReadOnly, IsAdminOrReadOnly

class CategoryListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

class RefundOrderView(generics.CreateAPIView, generics.ListAPIView):
    """Takes the two set of parameters: Order and Complaint
    
    Keyword arguments:
    order -- id of the order to be refunded
    complaint -- reason for the refund (compulsory)
    Return: status code 200
    """
    
    queryset = Refund.objects.all()
    serializer_class = RefundOrderSerializer
    permission_classes = [IsCustomerOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        order_id = self.request.data.get('order') 
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise ValidationError("Invalid Order ID")

        if order.owner != user:       # To make that user can only log a refund request for their own orders
            raise PermissionDenied("You do not have permission to log a complaint on this order.")

        serializer.save()
         