from django.db import models
from authApp.models import User
from vendor.models import Vendor
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ProductInventory(models.Model):
    quantity = models.IntegerField()
    #store Owner incoming
    
class Discount(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + str(self.percent)
    
    
class OrderDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    sku = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)
    inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)    
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

    
