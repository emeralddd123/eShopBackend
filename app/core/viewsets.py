from rest_framework import viewsets, status
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    CartItemSerializer,
    CartSerializer,
    AddCartItemSerializer,
    UpdateCartItemSerializer,
    CreateOrderSerializer,
    OrderSerializer,
    UpdateOrderSerializer,
    ImageSerializer,
)
from .models import Product, ProductCategory, Cart, CartItem, Order, Image
from authApp.models import User
from rest_framework.response import Response
from authApp.permissions import IsCustomer, IsVendorOrReadOnly, IsCustomerOrReadOnly, IsAdminOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsVendorOrReadOnly]

    # def create(self, serializer):
    #     try:
    #         vendor = self.request.user
    #         quantity = self.request.data.get("quantity")
    #         name = self.request.data.get("name")
    #         album = self.request.data.get("album")
    #         desc = self.request.data.get("desc")
    #         price = self.request.data.get("price")
    #         category_list = self.request.data.get("categories")
    #         img_album = ImageAlbum.objects.create()
    #         for image in album["images"]:
    #             Image.objects.create(
    #                 title=image["title"],
    #                 image=image["name"],
    #                 default=image["default"],
    #                 album=img_album,
    #             )
    #         categories = []
    #         for category in category_list:
    #             product_category = ProductCategory.objects.get(id=category["id"])
    #             categories.append(product_category)

    #         product = Product(
    #             vendor=vendor,
    #             quantity=quantity,
    #             name=name,
    #             album=img_album,
    #             desc=desc,
    #             price=price,
    #         )
    #         product.save()
    #         product.categories.set(categories)
    #         serializer = ProductSerializer(product)
    #         return Response(serializer.data, status=201)
    #     except Exception as e:
    #         return Response(
    #             {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )


class CartViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomerOrReadOnly]

    def create(self, request):
        user = self.request.user
        existing_cart = Cart.objects.filter(user=user).first()
        if existing_cart:
            serializer = CartSerializer(existing_cart)
            message = "User has an existing Cart"
            return Response(
                {"message": message, "data": serializer.data},
                status=status.HTTP_208_ALREADY_REPORTED,
            )

        cart = Cart(user=user)
        cart.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [IsCustomerOrReadOnly]

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer

        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer

        return CartItemSerializer


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "post", "delete", "options", "head"]
    permission_classes = [IsCustomerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data, context={"owner": self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        elif self.request.method == "PATCH":
            return UpdateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(owner=user)


# class ImageViewset(ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     #permission_classes = [IsVendorOrReadOnly]
    
