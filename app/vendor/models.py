from django.db import models
from authApp.models import Vendor

# Create your models here.


class VendorBalance(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="balance")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.email}'s Balance: {self.balance}"

class VendorStore(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="store")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
