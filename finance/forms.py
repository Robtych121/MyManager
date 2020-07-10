from django import forms
from .models import Account
import html5.forms.widgets as html5_widget

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'description', 'balance', 'currency')