from django.db import models
from authApp.models import User, Vendor, Customer



import random
# Create your views here.
def generate_sku(product_name):
  """Generates a unique SKU from the product name."""
  product_name_words = product_name.split(" ")
  sku = ""
  for word in product_name_words:
    sku += word[0]
  sku += str(random.randint(100000, 999999))
  return sku
# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False, null=False)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    desc = models.TextField()
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.percent)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    desc = models.TextField()
    sku = models.CharField(max_length=200, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def save(self):
        self.sku = generate_sku(self.name)
        super().save()
    
    class Meta:
        ordering = ['name', 'vendor']





class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_total(self, order_item_price):
        self.total += order_item_price
        self.save()
        
        
    def save(self):
        #self.totalling()
        super().save()
        
    def __str__(self):
        return  "{} made an order of {} at {}".format(self.user, self.total,self.updated_at)



class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.sub_total = self.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total(self.sub_total)

    def get_total_product_price(self):
        return self.quantity * self.product.price
