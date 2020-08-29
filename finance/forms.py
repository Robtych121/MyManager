from django import forms
from .models import Account, Period, Transcation
import html5.forms.widgets as html5_widget

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'description', 'balance', 'currency')


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('name', 'startDate', 'endDate', 'startBalance', 'endBalance', 'status')


class TranscationForm(forms.ModelForm):
    class Meta:
        model = Transcation
        fields = ('account', 'period', 'name', 'value', 'category', 'type', 'status', 'notes')