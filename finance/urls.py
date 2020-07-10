from django.contrib.auth import views
from django.urls import path
from .views import homepage, accounts_view, periods_view, create_or_edit_account, delete_account

urlpatterns = [
    path('', homepage, name="financehome"),
    path('view_accounts/', accounts_view, name="accounts_view"),
    path('view_periods/', periods_view, name="periods_view"),
    path('create_or_edit_account/', create_or_edit_account, name="create_or_edit_account"),
    path('delete_account/<int:id>', delete_account, name="delete_account"),
]