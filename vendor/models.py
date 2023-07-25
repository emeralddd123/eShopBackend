from django.db import models
from core.models import Vendor

# Create your models here.


class VendorBalance(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.store_name}'s Balance: {self.balance}"
