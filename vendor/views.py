from typing import Optional, List
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.response import Response
from .serializers import VendorSigninSerializer, VendorSignupSerializer
from .models import Vendor
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import AutoSchema

# Create your views here.

from django.contrib.auth.backends import ModelBackend

class VendorModelBackend(ModelBackend):
    UserModel = Vendor


def vendorauthenticate(authenticate, **kwargs):
    __get_backends = [VendorModelBackend]   

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        pass
    
@api_view(['POST'])
#@schema(CustomAutoSchema())
def vendorSignup(request):
    serializer = VendorSignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
#@schema(CustomAutoSchema())
def vendorLogin(request):
    serializer = VendorSigninSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    vendor = vendorauthenticate(
        request,
        email=serializer.validated_data['email'],
        password=serializer.validated_data['password'],
        **{'UserModel':Vendor}
    )
    print(vendor)
    if vendor is not None:
        login(request, user=vendor, backend=VendorModelBackend)
        return Response({'message': 'Login successful.'})
    return Response({'message': 'Invalid credentials or you are not a vendor. '}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendor(request):
    vendor =  request.vendor
    return Response({'vendor': vendor}, status=status.HTTP_200_OK)
