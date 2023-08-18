import os
import logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")
import django
django.setup()

from core.models import Image, ImageAlbum, Product, ProductCategory
from authApp.models import Vendor
import random


# Generate product data with image paths

vendor = Vendor.objects.get(username='vendor1')
product_data = [
    {"name": f"Product {i}", "desc": f"Description for Product {i}", "price": 129.99 + (i * 2.36), "image_path": f"zen/images/product100{i + 21}.jpg"}
    for i in range(30)
]

# Loop through the product_data and create Product instances
for data in product_data:
    # Create the ImageAlbum instance for the product
    album = ImageAlbum.objects.create()
    logging.info("Creating ImageAlbum")
    # Create the Image instance for the product
    image = Image.objects.create(
        name=data["name"],
        image=data["image_path"],
        default=True,  # Set default value as needed
        album=album,
        width=100,  # Set width value as needed
        length=100,  # Set length value as needed
    )
    logging.info('Image created')

    # Create the Product instance
    product = Product.objects.create(
        vendor=vendor,  # Replace your_vendor_instance with the actual vendor instance
        quantity=26,  # Replace your_quantity_value with the desired quantity
        name=data["name"],
        desc=data["desc"],
        price=data["price"],
        available=True,  # Set availability as needed
        album=album,  # Set the ImageAlbum for the Product
    )
    logging.info("{} created".format(product.name))

    # Add random categories to the product (between 1 and 5 categories)
    random_categories = ProductCategory.objects.order_by('?')[:random.randint(1, 5)]
    product.categories.set(random_categories)
    logging.info("{} set to {} categories".format(product.name, random_categories))