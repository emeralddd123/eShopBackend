from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings
from .forms import MyCustomAllAuthPasswordResetForm
from django.contrib.auth.forms import PasswordResetForm
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.db import models
from allauth.account import app_settings as allauth_account_settings
from allauth.utils import get_username_max_length

 
class Role(models.TextChoices):
        VENDOR = "VENDOR", "Vendor"
        CUSTOMER = "CUSTOMER", "Customer"
class MyCustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        if "allauth" in settings.INSTALLED_APPS:
            return MyCustomAllAuthPasswordResetForm
        else:
            return PasswordResetForm


class MyCustomRegisterSerializer(RegisterSerializer):
    """
    Added this custom serializer so that, user will be able to choose 
    if he want to be Vendor or Customer upon signup
    """

    role = serializers.ChoiceField(choices=Role.choices)
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'role': self.validated_data.get('role', '')
        }