from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nrouters

from .views import (
    ProductListView,
    ProductCreateView,
    ProductRetrieveView,
    ProductUpdateView,
    CategoryListView,
    CategoryCreateView,

)

from .viewsets import ProductCategoryViewSet, ProductViewSet, CartViewSet, CartItemViewSet, OrderViewSet
router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'categorys', ProductCategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

cart_router = nrouters.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", CartItemViewSet, basename="cart-items")

urlpatterns = [
    # path("products/", ProductListView.as_view(), name="product_list"),
    # path("products/create", ProductCreateView.as_view(), name="product_create"),
    # path("products/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    # path("products/retrieve/<int:pk>", ProductRetrieveView.as_view(), name="product_view"),
    # path("categories/", CategoryListView.as_view(), name="category_list"),
    # path("categories/create",CategoryCreateView.as_view(), name='category_create'),
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
    #path('cart/', AddProductToCart.as_view(), name="cart-add"),
    # path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    # path("orders/", OrderListView.as_view(), name="order-list"),
    # path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    # path("orders/update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
]

