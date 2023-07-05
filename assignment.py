# assign_products.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eshop.settings")

import django
django.setup()

from django.core.management import call_command
import random
from django.core.management.base import BaseCommand
from core.models import Product
from vendor.models import Vendor

class Command(BaseCommand):
    help = 'Assign products to vendors randomly'

    def handle(self, *args, **options):
        # Retrieve all vendors and products
        vendors = Vendor.objects.all()
        products = Product.objects.all()

        # Assign products to vendors randomly
        for product in products:
            vendor = random.choice(vendors)  # Choose a random vendor
            product.vendor = vendor  # Assign the vendor to the product
            product.save()

        self.stdout.write(self.style.SUCCESS('Products assigned to vendors successfully.'))
