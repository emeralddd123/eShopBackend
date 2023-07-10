from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductListView,
    ProductCreateView,
    ProductRetrieveView,
    ProductUpdateView,
    CategoryListView,
    CategoryCreateView,
    OrderDetailView,
    OrderListView,
    OrderUpdateView,
    OrderDeleteView,
)

from .viewsets import ProductCategoryViewSet, ProductViewSet
router = routers.DefaultRouter()

router.register(r'category', ProductCategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    # path("products/", ProductListView.as_view(), name="product_list"),
    # path("products/create", ProductCreateView.as_view(), name="product_create"),
    # path("products/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    # path("products/retrieve/<int:pk>", ProductRetrieveView.as_view(), name="product_view"),
    # path("categories/", CategoryListView.as_view(), name="category_list"),
    # path("categories/create",CategoryCreateView.as_view(), name='category_create'),
    path('', include(router.urls)),

    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    path("orders/update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
]

