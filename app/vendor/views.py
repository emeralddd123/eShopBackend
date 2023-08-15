from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.exceptions import NotAuthenticated, MethodNotAllowed
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
        vendor = (
            self.request.user
        )  # Assuming you have a OneToOneField for the vendor in your User model
        if vendor.is_authenticated and vendor.role == "VENDOR":
            balance = generics.get_object_or_404(VendorBalance, vendor=vendor)

            self.check_object_permissions(
                self.request, balance
            )  # Optional: Check object-level permissions if needed
            vendor_store = VendorStore.objects.filter(vendor=vendor).first()
            print(vendor_store)
            store_data = VendorStoreSerializer(vendor_store).data
            balance_data = VendorBalance(balance).data

            return Response(
                content_type="application/json",
                data={"store": store_data, "balance": balance_data},
            )
        else:
            return Response(
                content_type="application/json",
                status=403,
                data="Only Vendor Can Perform This Task",
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
            content_type="application/json",
            data={"store": store_data.data, "products": store_products.data},
        )


class VendorListView(generics.ListAPIView):
    serializer_class = VendorStoreSerializer
    queryset = VendorStore.objects.all()
