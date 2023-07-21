from django.urls import path, include

from . import views

urlpatterns = [
    path('signup', views.signup, name="registration"),
    path('login/', views.login, name="login"),
    path('vsignup/', views.vendorSignup, name="vendor-registration"),
    path('vlogin/', views.vendorLogin, name="vendor-login"),
    path('verify_token/', views.test_token, name='verify-token'),
    path('user/', views.info , name='user-info'),
    path('logout/', views.logout, name='logout'),
    
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
