from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    #path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    #path('', include('djoser.social.urls')),
]
