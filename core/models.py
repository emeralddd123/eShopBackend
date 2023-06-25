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


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    sku = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Discount(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.percent)


class Order(models.Model):
    items = models.ManyToManyField(Product, through="OrderItem")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + " made an order of {self.total} at {self.updated_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
