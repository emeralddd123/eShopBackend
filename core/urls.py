from django.urls import path, include
from .views import (
    ProductListView,
    ProductCreateView,
    ProductRetrieveView,
    ProductUpdateView,
    CategoryListView,
    CartUpdateView,
    CartRetrieveView,
    CartDeleteView,
    OrderCreateView,
    OrderDetailView,
    OrderListView,
    OrderUpdateView,
    OrderDeleteView,
    CartCreateView
)

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create", ProductCreateView.as_view(), name="product_create"),
    path("products/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("products/retrieve/<int:pk>", ProductRetrieveView.as_view(), name="product_view"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("cart/create", CartCreateView.as_view(), name="cart_create"),
    path("cart/update/<int:pk>/", CartUpdateView.as_view(), name="cart-update"),
    path("cart/retrieve/<int:pk>/", CartRetrieveView.as_view(), name="cart-retrieve"),
    path("cart/delete/<int:pk>/", CartDeleteView.as_view(), name="cart-delete"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    path("orders/update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
]

