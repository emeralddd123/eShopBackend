from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


    
class User(AbstractUser):
    class Role(models.TextChoices):
        VENDOR = "VENDOR", "Vendor"
        CUSTOMER = "CUSTOMER", "Customer"
        
    #base_role = Role.CUSTOMER
    role = models.CharField(max_length=50, choices=Role.choices)
    
    USERNAME_FIELD = 'username'
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         #self.role = self.base_role
    #         return super().save(*args, **kwargs)


class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.CUSTOMER)


class Customer(User):
    base_role = User.Role.CUSTOMER
    customers = CustomerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for customer"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

class VendorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.VENDOR)


class Vendor(User):
    base_role = User.Role.VENDOR
    vendors = VendorManager()

    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        from vendor.models import VendorBalance
        # Call the base class's save() method
        super(Vendor, self).save(*args, **kwargs)

        # Create VendorBalance instance if it doesn't exist
        VendorBalance.objects.get_or_create(vendor=self, defaults={'balance': 0})

    def welcome(self):
        return "Only for Vendor"


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.city}, {self.country}"



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
