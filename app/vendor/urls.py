from django.urls import path, include
from .views import VendorBalanceView, VendorStoreView
urlpatterns = [
   path('balance', VendorBalanceView.as_view(), name='vendor-balance'),
   #path('info', VendorInfoView.as_view(), name='vendor-info'),
   path('store/<pk>', VendorStoreView.as_view(), name='vendor-store')

]