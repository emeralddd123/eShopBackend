from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from .serializers import VendorStoreSerializer, VendorBalanceSerializer
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
    
class VendorStoreView(generics.CreateAPIView, generics.RetrieveAPIView):
    serializer_class = VendorStoreSerializer
    
    def get_queryset(self):
        vendor_store = VendorStore.objects.filter(vendor=self.request.user).first()
        return vendor_store
    
    def perform_create(self, serializer):
        vendor = self.request.user
        serializer.save(vendor=vendor)
    
    
# class VendorInfoView(generics.RetrieveAPIView):
#     serializer_class = VendorInfoSerializer
    
#     def get_object(self):
#         vendor = self.request.user
#         if vendor.is_authenticated:
#             return vendor
#         else: 
#             raise NotAuthenticated

