from django.urls import path, include
from .views import VendorView, VendorStoreView, VendorListView
urlpatterns = [
   path('info', VendorView.as_view(), name='vendor-info'),
   #path('info', VendorInfoView.as_view(), name='vendor-info'),
   path('store/<int:pk>', VendorStoreView.as_view(), name='vendor-store'),
   path('store', VendorListView.as_view(), name='vendor-list')

]