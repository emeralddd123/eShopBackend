from rest_framework import viewsets
from .serializers import ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory
from authApp.models import User
from rest_framework.response import Response

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, serializer):
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
        return Response(status=201)