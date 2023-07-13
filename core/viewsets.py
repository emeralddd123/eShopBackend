from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    CartItemSerializer,
    CartSerializer,
    AddCartItemSerializer,
    UpdateCartItemSerializer,
    CreateOrderSerializer,
    OrderItemSerializer,
    OrderSerializer,
    UpdateOrderSerializer,
    
)
from .models import Product, ProductCategory, Cart, CartItem, Order
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


class CartViewSet(CreateModelMixin,RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    
    http_method_names = ["get", "post", "patch", "delete"]
    
    def get_queryset(self):
        print(self.kwargs)
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}


class OrderViewSet(ModelViewSet):
    
    http_method_names = ["get", "patch", "post", "delete", "options", "head"]
    
    # def get_permissions(self):
    #     if self.request.method in ["PATCH", "DELETE"]:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]
            
    
    
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={"owner": self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
        
    

    
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer
       
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(owner=user)