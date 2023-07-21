from rest_framework import serializers
from django.db import transaction


from .models import (
    Product,
    Discount,
    Order,
    OrderItem,
    ProductCategory,
    Cart,
    CartItem,
    Image,
    ImageAlbum,
)
from authApp.models import User, Vendor


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        # fields = ['id', 'name', 'image', 'default']
        fields = "__all__"

class SummaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields = ['name', 'image', 'default']

class ImageAlbumSerializer(serializers.ModelSerializer):
    images = SummaryImageSerializer(many=True)

    class Meta:
        model = ImageAlbum
        fields = ["id", "images"]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "desc"]
        excludes = ["created_at", "updated_at"]


class SummaryProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id"]
        read_only = True


class ProductSerializer(serializers.ModelSerializer):
    categories = SummaryProductCategorySerializer(many=True)
    album = ImageAlbumSerializer(many=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "vendor",
            "quantity",
            "name",
            "album",
            "desc",
            "sku",
            "price",
            "categories",
        ]
        #depth = 1
        read_only_fields = ["id", "sku"]


class SummaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SummaryProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "sub_total"]

    def total(self, cartitem: CartItem):
        return cartitem.quantity * cartitem.product.price


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                "There is no product associated with the given ID"
            )

        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]

        try:
            cartitem = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()

            self.instance = cartitem

        except:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data
            )

        return self.instance

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]


class UpdateCartItemSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = CartItem
        fields = ["quantity"]


class SummaryCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name="main_total")

    class Meta:
        model = Cart
        fields = ["id", "items", "grand_total"]

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total


class OrderItemSerializer(serializers.ModelSerializer):
    product = SummaryProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "placed_at", "pending_status", "owner", "items"]


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("This cart_id is invalid")

        elif not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError("Sorry your cart is empty")

        return cart_id

    def save(self, *args, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            user_id = self.context["owner"]
            order = Order.objects.create(owner_id=user_id)
            cartitems = CartItem.objects.filter(cart_id=cart_id)
            orderitems = [
                OrderItem(order=order, product=item.product, quantity=item.quantity)
                for item in cartitems
            ]
            OrderItem.objects.bulk_create(orderitems)
            Cart.objects.filter(id=cart_id).delete()
            return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pending_status"]
