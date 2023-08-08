from django.db import models
from authApp.models import User, Vendor, Customer
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import generate_sku, get_upload_path
from django.utils import timezone


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(
        ImageAlbum,
        blank=True,
        null=True,
        related_name="images",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        super(Image, self).save(*args, **kwargs)


# Signal function to create an ImageAlbum instance for each new Image instance
@receiver(post_save, sender=Image)
def create_image_album(sender, instance, created, **kwargs):
    if created and not instance.album:
        album = ImageAlbum.objects.create()
        instance.album = album
        instance.save()


# models.py - Connect the signal
post_save.connect(create_image_album, sender=Image)


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
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
    id = models.AutoField(primary_key=True, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    album = models.OneToOneField(
        ImageAlbum, related_name="model", on_delete=models.CASCADE
    )
    desc = models.TextField()
    sku = models.CharField(max_length=200, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(
        ProductCategory, related_name="products", blank=True
    )
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.sku = generate_sku(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name", "vendor"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]


class Order(models.Model):
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"

    PAYMENT_STATUS_CHOICES = [
        (PENDING, "PENDING"),
        (COMPLETE, "COMPLETE"),
        (FAILED, "FAILED"),
    ]
    id = models.UUIDField(primary_key=True,unique=True, default=uuid4())
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_CHOICES, default="PENDING"
    )
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT)
    processed = models.BooleanField(default=False)
    return_status = models.BooleanField(default=False)

    def __str__(self):
        return self.pending_status

    def save(self, *args, **kwargs):            
        super().save()

    def __str__(self):
        return "{} made an order of {} at {}".format(
            self.owner, self.pending_status, self.placed_at
        )



class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, related_name="products", on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="cartitems",
    )
    quantity = models.PositiveIntegerField(default=0)


class Refund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    complaint = models.TextField(blank=False, null=False)
    