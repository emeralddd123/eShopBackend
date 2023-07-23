from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404
from .models import User, Vendor, Customer
from rest_framework.authtoken.models import Token

# from .serializers import CreateUserSerializer, UserSerializer

# @api_view(['POST'])
# def signup(request):
#     serializer = CreateUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = Customer.objects.get(username=serializer.validated_data['username'])
#         user.set_password(serializer.validated_data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token': token.key, 'user': serializer.data})
#     return Response(serializer.errors, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response("missing user", status=status.HTTP_404_NOT_FOUND)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(user)
#     return Response({'token': token.key, 'user': serializer.data})

# @api_view(['POST'])
# def vendorSignup(request):
#     serializer = CreateUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = Vendor.objects.get(username=request.data['username'])
#         user.set_password(request.data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token': token.key, 'user': serializer.data})
#     return Response(serializer.errors, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def vendorLogin(request):
#     user = get_object_or_404(Vendor, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response("missing user", status=status.HTTP_404_NOT_FOUND)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(user)
#     return Response({'token': token.key, 'user': serializer.data})

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     return Response("passed!")


# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# def info(request):
#     username = request.user.username
#     user = get_object_or_404(User, username=username)
#     serializer = UserSerializer(user)
#     return Response({'user':serializer.data})

# @authentication_classes([TokenAuthentication])
# @api_view(['POST'])
# def logout(request):
#     user = request.user
#     token = get_object_or_404(Token, user=user)
#     token.delete()
#     return Response({'message':'logout succesful'})
    