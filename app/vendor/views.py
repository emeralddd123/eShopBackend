from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorStoreSerializer, VendorBalanceSerializer
from .models import VendorBalance, VendorStore
from core.models import Product
from core.serializers import SummaryProductSerializer, ProductSerializer


class VendorView(generics.RetrieveUpdateAPIView):
    serializer_class = VendorStoreSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        vendor = self.request.user
        if vendor.is_authenticated and vendor.role == "VENDOR":
            balance = generics.get_object_or_404(VendorBalance, vendor=vendor)

            self.check_object_permissions(self.request, balance)
            vendor_store = VendorStore.objects.filter(vendor=vendor).first()
            print(vendor_store)
            store_data = VendorStoreSerializer(vendor_store).data
            balance_data = VendorBalance(balance).data

            return Response(
                data={"store": store_data, "balance": balance_data},
            )
        else:
            raise PermissionDenied(
                detail="Only Vendor Are Allowed to perfom this action"
            )


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
