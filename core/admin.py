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
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'quantity', 'price']
    list_filter = ['categories', 'created_at']
    search_fields = ['name', 'desc', 'sku']
    ordering = ['name', 'created_at']
    prepopulated_fields = {'sku':('name',)}
    raw_id_fields = ['vendor']
    
    
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(CartItem)


    
    
