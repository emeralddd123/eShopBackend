import os
import uuid
import random


# Create your views here.
def generate_sku(product_name):
    """Generates a unique SKU from the product name."""
    product_name = product_name.strip()
    product_name_words = product_name.split(" ")
    sku = ""
    for word in product_name_words:
        sku += word[0]
    sku += str(random.randint(100000, 999999))
    return sku


def get_unique_filename(instance, filename):
    # Generate a random filename using UUID
    ext = filename.split(".")[-1]
    random_filename = f"{uuid.uuid4().hex}.{ext}"
    return random_filename


def get_upload_path(instance, filename):
    # Custom function to determine the upload path for the image
    timestamp_subdir = instance.created_at.strftime("%Y/%m/%d")
    unique_filename = get_unique_filename(instance, filename)
    return os.path.join("images/products", timestamp_subdir, unique_filename)
