from rest_framework import serializers
from django.db import transaction
from decimal import Decimal


from .models import (
    Product,
    Discount,
    Order,
    OrderItem,
    ProductCategory,
    Cart,
    CartItem,
    Image,
    Refund,
)

from vendor.models import VendorBalance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        # fields = ['id', 'title', 'image', 'default']
        fields = "__all__"


class SummaryImageSerializer(serializers.ModelSerializer):
    default = serializers.BooleanField()

    class Meta:
        model = Image
        fields = ["title", "image", "default"]



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "desc"]
        excludes = ["created_at", "updated_at"]


class SummaryProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name"]
        read_only = True


class ProductSerializer(serializers.ModelSerializer):
    categories = SummaryProductCategorySerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "vendor",
            "quantity",
            "name",
            "images",
            "desc",
            "sku",
            "price",
            "categories",
        ]
        read_only_fields = ["id", "vendor", "sku"]
        
    def create(self, validated_data):
        images = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for image in images:
            new_image = Image.objects.create(product=product, image=image)
            new_image.save()
        return product


class SummaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SummaryProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="sub_totall")

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "sub_total"]

    def sub_totall(self, cartitem: CartItem):
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
        # read_only_fields = ["id"]

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total


class OrderItemSerializer(serializers.ModelSerializer):
    product = SummaryProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name="sub_totall")

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "sub_total"]

    def sub_totall(self, orderItem: OrderItem):
        return orderItem.product.price * orderItem.quantity


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField(method_name="get_total")

    class Meta:
        model = Order
        fields = [
            "id",
            "placed_at",
            "pending_status",
            "return_status",
            "owner",
            "items",
            "total",
        ]
        read_only_fields = ["id", "return_status"]

    def get_total(self, order: Order):
        items = order.items.all()
        return sum(item.product.price * item.quantity for item in items)


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
            orderitems = []

            for item in cartitems:
                product = item.product
                quantity_ordered = item.quantity

                # Check if there's enough quantity in the inventory
                if product.quantity < quantity_ordered:
                    raise serializers.ValidationError(
                        f"Insufficient quantity for product: {product.name}"
                    )

                # Create the order item
                order_item = OrderItem(
                    order=order, product=product, quantity=quantity_ordered
                )
                orderitems.append(order_item)

                # Deduct the quantity from the product inventory
                product.quantity -= quantity_ordered
                product.save()

                # Update the vendor's balance
                vendor = product.vendor
                vendor_balance = VendorBalance.objects.get(vendor=vendor)
                total_sale_amount = product.price * quantity_ordered
                vendor_balance.balance += total_sale_amount * Decimal(
                    "0.95"
                )  # 5% commision goes to the management
                vendor_balance.save()

            OrderItem.objects.bulk_create(orderitems)

            Cart.objects.filter(id=cart_id).delete()

            return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pending_status"]


class RefundOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = "__all__"
        read_only_fields = ["id"]
