from django.contrib import admin
from .models import Vendor, VendorBalance
# Register your models here.

admin.site.register(Vendor)
admin.site.register(VendorBalance)
