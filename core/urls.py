from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nrouters
from .views import RefundOrderView


from .viewsets import ProductCategoryViewSet, ProductViewSet, CartViewSet, CartItemViewSet, OrderViewSet
router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'categorys', ProductCategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

cart_router = nrouters.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", CartItemViewSet, basename="cart-items")

urlpatterns = [

    path('', include(router.urls)),
    path('', include(cart_router.urls)),
    path('request-order', RefundOrderView.as_view(), name='request-refund')

]

