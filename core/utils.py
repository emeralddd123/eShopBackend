import os, uuid, random
from decimal import Decimal
from django.db import transaction
from vendor.models import VendorBalance


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


def returnedOrderResolution(order):
    # function to return the items in a returned to Inventory and also deduct
    # the money from the order from respective vendor
    # will be expecting order_id with paid status complete as a parameter

    orderitems = order.items.all()
    with transaction.atomic():
        for orderitem in orderitems:
            product = orderitem.product
            quantity = orderitem.quantity
            product.quantity += quantity
            vendor_id = orderitem.product.vendor.id
            product_price = orderitem.product.price
            product.save()

            commisioned_price = product_price * quantity * Decimal("0.95")
            vendor_balance = VendorBalance.objects.get(vendor=vendor_id)
            vendor_balance.balance -= commisioned_price
            vendor_balance.save()

        order.return_status = True
        order.save()
