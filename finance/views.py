from django.shortcuts import render
from .models import Account

# Create your views here.
def homepage(request):
    return render(request, 'financehome.html')


def accounts_view(request):
    accounts = Account.objects.all()

    return render(request, 'accounts_view.html', {'accounts': accounts})