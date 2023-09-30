from django.dispatch import receiver
from djoser.signals import user_registered
from .models import VendorBalance, VendorStore


@receiver(user_registered)
def initiate_vendor_balance(user, request):
    print('balance created!!!!!!!')
    if user.role == "VENDOR":
        vendor_balance = VendorBalance(user=user)
        vendor_balance.save()


@receiver(user_registered)
def initiate_vendor_store(user, request):
    print('store created!!!!!!!')
    if user.role == "VENDOR":
        store_name = user.username + "_store"
        description = "Default Store Description"

        vendor_store = VendorStore(user=user, name=store_name, description=description)
        vendor_store.save()
