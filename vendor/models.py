from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class Vendor(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    store_name = models.CharField(max_length=255,unique=True, blank=False)
    description = models.CharField(max_length=255, blank=True)
    
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'store_name']
    
    
    def __str__(self):
        return self.store_name
        

class VendorBalance(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vendor.store_name}'s Balance: {self.balance}"
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    