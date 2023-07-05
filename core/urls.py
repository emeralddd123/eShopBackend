from django.urls import path, include
from .views import ProductListView, CategoryListView

urlpatterns = [
        path('products/', ProductListView.as_view(), name='product_list'),
        path('categories/', CategoryListView.as_view(), name='category_list'),

]