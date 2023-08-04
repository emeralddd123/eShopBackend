from rest_framework.serializers import ModelSerializer, Serializer
from .models import VendorBalance, VendorStore
from authApp.models import User, Vendor


class sUserSerializer(ModelSerializer):
    class Meta:
        model=User
        
        
class sVendorSerializer(ModelSerializer):
    class Meta(sUserSerializer.Meta):
        model = Vendor
        fields = ['username', 'email', 'role']
        exclude_fields = ['id']
        
class VendorBalanceSerializer(ModelSerializer):
    class Meta:
        model = VendorBalance
        fields = ['balance', 'updated_at']
        read_only_fields = ['balance', 'updated_at']
        
        
        
class SummaryVendorStoreSerializer(ModelSerializer):
    
    class Meta:
        model = VendorStore
        fields = ['name', 'description']
        read_only_fields = ['vendor',]
        
        
class VendorInfoSerializer(Serializer):
    vendor = sVendorSerializer()
    balance = VendorBalanceSerializer()
    store_info = SummaryVendorStoreSerializer()
    
    class Meta:
        fields = ['vendor','balance', 'store_info']