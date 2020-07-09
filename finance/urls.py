from django.contrib.auth import views
from django.urls import path
from .views import homepage, accounts_view

urlpatterns = [
    path('', homepage, name="financehome"),
    path('view_accounts/', accounts_view, name="accounts_view"),
]