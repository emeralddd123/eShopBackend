from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name="registration"),
    path('login', views.login, name="login"),
    path('verify_token', views.test_token, name='verify-token'),
]
