from django.shortcuts import render
from .models import Account, Period

# Create your views here.
def homepage(request):
    return render(request, 'financehome.html')


def accounts_view(request):
    accounts = Account.objects.all()

    return render(request, 'accounts_view.html', {'accounts': accounts})


def periods_view(request):
    periods = Period.objects.all()

    return render(request, 'periods_view.html', {'periods': periods})