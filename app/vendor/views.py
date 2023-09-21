from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorStoreSerializer, VendorBalanceSerializer
from .models import VendorBalance, VendorStore
from core.models import Product
from core.serializers import SummaryProductSerializer, ProductSerializer
from authApp.permissions import IsVendorOrReadOnly, IsVendor


class VendorView(generics.RetrieveUpdateAPIView):
    serializer_class = VendorStoreSerializer
    permission_classes = [IsVendorOrReadOnly]

    def get_object(self):
        vendor = self.request.user
        vendor_store = VendorStore.objects.get(vendor=vendor)
        # store_data = VendorStoreSerializer(vendor_store).data

        # vendor_balance = VendorBalance.objects.get(vendor=vendor)
        # balance_data = VendorBalanceSerializer(vendor_balance).data

        # response_data = {"store_data": store_data, "balance_data": balance_data}
        return vendor_store


class VendorStoreView(generics.RetrieveAPIView):
    serializer_class = VendorStoreSerializer
    queryset = VendorStore.objects.all()
    lookup_field = "pk"

    def get(self, request, pk):
        vendor_store = VendorStore.objects.get()
        vendor_products = Product.objects.filter(vendor=vendor_store.vendor)
        print(vendor_products)
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
        vendor_balance = VendorBalance.objects.get(vendor=vendor)
        return vendor_balance
    