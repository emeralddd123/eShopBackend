from django.db import transaction
from authApp.models import Vendor
from .models import VendorBalance
from decimal import Decimal
from django.db.models import F



def updateProductInventory(order):
    try:
        orderitems = order.items.all()
        for orderitem in orderitems:
            product = orderitem.product
            product.quantity -= orderitem.quantity
            product.save()
    except Exception as e:
        # Handle specific exceptions if needed, such as DatabaseError or ValidationError
        # Log the error or perform any necessary actions
        print(f"Error occurred: {e}")
        
        
@transaction.atomic
def updateVendorBalance(order):  # get a Order object and loop through the items in it and add the price of it to the vendor's account
    # orderitems = order.items.all()
    # for orderitem in orderitems:
    #     vendor_id = orderitem.product.vendor.id
    #     product_price = orderitem.product.price
    #     quantity = orderitem.quantity
    #     salePrice = product_price*quantity
    #     commisioned_price = salePrice*Decimal('0.95')   #5 percent commisioned is being removed from  each sales 
    #     vendor_balance = VendorBalance.objects.get(vendor=vendor_id)
    #     vendor_balance.balance += commisioned_price
    #     vendor_balance.save()    
    print('uncomment the real function in vendor utils')