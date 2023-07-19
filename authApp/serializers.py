from .models import User
from django.db import models
from rest_framework import serializers


 
class Role(models.TextChoices):
        VENDOR = "VENDOR", "Vendor"
        CUSTOMER = "CUSTOMER", "Customer"
class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email', 'role']

