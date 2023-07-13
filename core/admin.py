from django.contrib import admin
from .models import (
    Product,
    ProductCategory,
    Order,
    OrderItem,
    Discount,
    CartItem,
    Cart
)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(CartItem)

