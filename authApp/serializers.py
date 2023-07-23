from .models import User
from django.db import models
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer, UserSerializer as DjoserUserSerializer



 
class Role(models.TextChoices):
        VENDOR = "VENDOR", "Vendor"
        CUSTOMER = "CUSTOMER", "Customer"
class UserCreateSerializer(DjoserUserCreateSerializer):
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password' ,'email', 'role']


class UserSerializer(DjoserUserSerializer):
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta(DjoserUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'role']
        