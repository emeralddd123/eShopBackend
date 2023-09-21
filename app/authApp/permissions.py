from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import User

from rest_framework.permissions import IsAuthenticated

class IsVendorOrReadOnly(BasePermission):
    message = "Only Vendors Are Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is a vendor
        if request.user.is_authenticated and request.user.role=="VENDOR":
            return True

        raise PermissionDenied(self.message)
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is a vendor and owns the product
        if request.user.is_authenticated and request.user.role=="VENDOR" and obj.vendor == request.user:
            return True
        elif obj.vendor != request.user:
            raise PermissionDenied("This Product Does not belong to you")
        raise PermissionDenied(self.message)
     

from rest_framework.permissions import BasePermission

class IsCustomerOrReadOnly(BasePermission):
    message = "Only Customers Are Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if request.user.is_authenticated and request.user.role == "CUSTOMER":
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.role == "CUSTOMER":
            try:
                return obj.owner == request.user      #TODO: a mees caused by my inconsistent naming, will fix later
            except AttributeError as e:
                return obj.user == request.user
        
        return False 


class IsAdminOrReadOnly(BasePermission):
    message = "Only Admins Are Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is an admin
        if request.user.is_authenticated and request.user.is_admin and request.user.role=="ADMIN":
            return True
        raise PermissionDenied(self.message)
    

    
class IsVendor(BasePermission):
    message = "Only Vendor Is Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Check if the user is a vendor
        if request.user.is_authenticated and request.user.role=="VENDOR":
            return True

        raise PermissionDenied(self.message)
    def has_object_permission(self, request, view, obj):
        # Check if the user is a vendor and owns the product
        if request.user.is_authenticated and request.user.role=="VENDOR" and obj.vendor == request.user:
            return True
        raise PermissionDenied(self.message)
     

class IsCustomer(BasePermission):
    message = "Only Customers Are Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Check if the user is a customer
        is_user = IsAuthenticated().has_permission(request, view)
        is_customer = request.user.role == "CUSTOMER"
        if is_user and is_customer:
            return True
        raise PermissionDenied(self.message)
    
    # def has_object_permission(self, request, view, obj):
    #     # Check if the user is a customer and owns the cart
    #     if request.user.is_authenticated and request.user.role=="CUSTOMER" and obj.owner == request.user:
    #         return True
        #raise PermissionDenied(self.message)

class IsAdmin(BasePermission):
    message = "Only Admins Are Allowed to perform this action"
    
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.is_authenticated and request.user.is_admin and request.user.role=="ADMIN":
            return True
        raise PermissionDenied(self.message)