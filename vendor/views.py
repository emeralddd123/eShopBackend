from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from .serializers import SummaryVendorStoreSerializer, VendorBalanceSerializer, VendorInfoSerializer
from .models import VendorBalance, VendorStore

class VendorBalanceView(generics.RetrieveAPIView):
    serializer_class = VendorBalanceSerializer
    
    def get_object(self):
        vendor = self.request.user # Assuming you have a OneToOneField for the vendor in your User model
        if vendor.is_authenticated:
            obj = generics.get_object_or_404(VendorBalance, vendor=vendor)

            self.check_object_permissions(self.request, obj)  # Optional: Check object-level permissions if needed

            return obj
        else: 
            raise NotAuthenticated
    
class VendorInfoView(generics.RetrieveAPIView):
    serializer_class = VendorInfoSerializer
    
    def get_object(self):
        vendor = self.request.user
        if vendor.is_authenticated:
            return vendor
        else: 
            raise NotAuthenticated