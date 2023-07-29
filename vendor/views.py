from authApp.models import Vendor
from .models import VendorBalance

def updateProductInventory(order):  # get the inventory and update the items remaining in the store
    orderitems = order.items.all()
    for orderitem in orderitems:
        vendor_id = orderitem.product.vendor
        quantity = orderitem.quantity
        vendor = Vendor.objects.get(id=vendor_id)
        vendor_balance = VendorBalance.objects.get(vendor=vendor)
        
    pass


def updateVendorBalance():  # get a Order object and loop through the items in it and add the price of it to the vendor's account
    pass

