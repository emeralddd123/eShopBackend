from django.db import models
from authApp.models import Vendor

# Create your models here.


class VendorBalance(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="vendor")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.store_name}'s Balance: {self.balance}"

class VendorStore(models.Model):
    user = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    vendor_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)