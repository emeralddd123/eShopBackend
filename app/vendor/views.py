from rest_framework import generics
from rest_framework.response import Response
from .serializers import VendorStoreSerializer, VendorBalanceSerializer
from .models import VendorBalance, VendorStore
from core.models import Product
from core.serializers import SummaryProductSerializer, ProductSerializer
from authApp.permissions import IsVendorOrReadOnly, IsVendor
from rest_framework.generics import get_object_or_404



class VendorView(generics.RetrieveUpdateAPIView):
    serializer_class = VendorStoreSerializer
    permission_classes = [IsVendorOrReadOnly]

    def get_object(self):
        vendor = self.request.user
        vendor_store = VendorStore.objects.get(vendor=vendor)
        return vendor_store


class VendorStoreView(generics.RetrieveUpdateAPIView):
    serializer_class = VendorStoreSerializer
    queryset = VendorStore.objects.all()
    permission_classes = [IsVendorOrReadOnly]
    lookup_field = "pk"

    def get(self, request, pk):
        vendor_store = get_object_or_404(VendorStore, pk=pk)
        vendor_products = Product.objects.filter(vendor=vendor_store.vendor)
        store_data = VendorStoreSerializer(vendor_store)
        store_products = ProductSerializer(vendor_products, many=True)
        return Response(
            data={"store": store_data.data, "products": store_products.data},
        )


class VendorListView(generics.ListAPIView):
    serializer_class = VendorStoreSerializer
    queryset = VendorStore.objects.all()


class VendorBalanceView(generics.RetrieveAPIView):
    serializer_class = VendorBalanceSerializer
    queryset = VendorBalance.objects.all()
    permission_classes = [IsVendor]
    
    def get_object(self):
        vendor = self.request.user
        vendor_balance, created = VendorBalance.objects.get_or_create(vendor=vendor)
        return vendor_balance
    