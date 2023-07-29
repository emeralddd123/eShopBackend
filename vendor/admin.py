from django.contrib import admin
from .models import VendorBalance, VendorStore
# Register your models here.

admin.site.register(VendorBalance)
admin.site.register(VendorStore)
