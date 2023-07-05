from .models import Vendor
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


class VendorSignupSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'email', 'password', 'store_name', 'description']
        extra_kwargs = {'password': {'write_only': True}} 
    def create(self, validated_data): 
        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password'])                          
            vendor = Vendor.objects.create(
                  username=validated_data['username'],
                  email=validated_data['email'],
                  store_name=validated_data['store_name'],
                  description=validated_data['description'],
                  password=password)
        return vendor
    


class VendorSigninSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields =  ['email', 'password', ]
        
        