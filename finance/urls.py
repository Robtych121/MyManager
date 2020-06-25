from django.contrib.auth import views
from django.urls import path
from .views import homepage

urlpatterns = [
    path('', homepage, name="financehome"),
]