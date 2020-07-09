from django.contrib.auth import views
from django.urls import path
from .views import homepage, accounts_view, periods_view

urlpatterns = [
    path('', homepage, name="financehome"),
    path('view_accounts/', accounts_view, name="accounts_view"),
    path('view_periods/', periods_view, name="periods_view"),
]