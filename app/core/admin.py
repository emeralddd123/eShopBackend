from django.contrib import admin
from .models import (
    Product,
    ProductCategory,
    Order,
    OrderItem,
    Discount,
    CartItem,
    Cart,
    Image,
    Refund
)

# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

    

class ProductAdmin(admin.ModelAdmin):
    models = Product
    list_display = ['sku', 'name', 'quantity', 'price']
    list_filter = ['categories', 'created_at']
    search_fields = ['name', 'desc', 'sku']
    ordering = ['name', 'created_at']
    prepopulated_fields = {'sku':('name',)}
    raw_id_fields = ['vendor']
    readonly_fields = ['created_at']
    inlines = [ImageInline]

class CartItemInline(admin.StackedInline):
    model = CartItem
    extra = 1
    
class CartAdmin(admin.ModelAdmin):
    model = Cart
    inlines = [CartItemInline]
    raw_id_fields = ['user']

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra =1
    
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    raw_id_fields = ['owner']
    
    
admin.site.register(Image)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Refund)


    
    
