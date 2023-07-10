from django.contrib import admin
from .models import (
    Product,
    ProductCategory,
    Order,
    OrderItem,
    Discount,
)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
