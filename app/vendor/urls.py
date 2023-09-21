from django.urls import path, include
from .views import VendorView, VendorStoreView, VendorListView, VendorBalanceView
urlpatterns = [
   path('info', VendorView.as_view(), name='vendor-info'),
   #path('info', VendorInfoView.as_view(), name='vendor-info'),
   path('store/<int:pk>', VendorStoreView.as_view(), name='vendor-store'),
   path('store', VendorListView.as_view(), name='vendor-list'),
   path('balance', VendorBalanceView.as_view(), name='vendor-balance')

]