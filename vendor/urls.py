from django.urls import path, include
from .views import VendorBalanceView, VendorInfoView
urlpatterns = [
   path('balance', VendorBalanceView.as_view(), name='vendor-balance'),
   path('info', VendorInfoView.as_view(), name='vendor-info'),

]