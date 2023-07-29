from authApp.models import Vendor
from .models import VendorBalance

def updateProductInventory(order):  # get the inventory and update the items remaining in the store
    orderitems = order.items.all()
    for orderitem in orderitems:
        product = orderitem.product
        product.quantity -= orderitem.quantity
        product.save()
        

def updateVendorBalance(order):  # get a Order object and loop through the items in it and add the price of it to the vendor's account
    orderitems = order.items.all()
    for orderitem in orderitems:
        vendor_id = orderitem.product.vendor.id
        product_price = orderitem.product.price
        quantity = orderitem.quantity
        salePrice = product_price*quantity
        commisioned_price = salePrice*0.95   #5 percent commisioned is being removed from  each sales 
        vendor_balance = VendorBalance.objects.get(vendor=vendor_id)
        vendor_balance.balance =+ commisioned_price
        vendor_balance.save()
