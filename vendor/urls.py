from django.urls import path, include
from .views import vendorLogin, vendorSignup, vendor

urlpatterns = [
        path('register/', vendorSignup, name='register_vendor'),
        path('login/', vendorLogin, name='login_vendor'),
        path('',vendor, name='vendor' )

]