from django.contrib.auth import views
from django.urls import path
from .views import homepage, accounts_view, periods_view, create_or_edit_account, delete_account, view_detailed_account, update_balance_account, create_or_edit_period, delete_period, view_detailed_period, update_balance_period, transcations_view

urlpatterns = [
    path('', homepage, name="financehome"),
    path('view_accounts/', accounts_view, name="accounts_view"),
    path('view_periods/', periods_view, name="periods_view"),
    path('create_account/', create_or_edit_account, name="create_or_edit_account"),
    path('edit_account/<int:pk>', create_or_edit_account, name="create_or_edit_account"),
    path('delete_account/<int:id>', delete_account, name="delete_account"),
    path('view_detailed_account/<int:id>', view_detailed_account, name="view_detailed_account"),
    path('update_balance_account/<int:id>', update_balance_account, name="update_balance_account"),
    path('create_period/', create_or_edit_period, name="create_or_edit_period"),
    path('delete_period/<int:id>', delete_period, name="delete_period"),
    path('edit_period/<int:pk>', create_or_edit_period, name="create_or_edit_period"),
    path('view_detailed_period/<int:id>', view_detailed_period, name="view_detailed_period"),
    path('update_balance_period/<int:id>', update_balance_period, name="update_balance_period"),
    path('transcations_view/', transcations_view, name="transcations_view"),
]