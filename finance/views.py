from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Period, Transcation
from .forms import AccountForm
from django.db.models import Sum

# Create your views here.
def homepage(request):
    return render(request, 'financehome.html')


def accounts_view(request):
    accounts = Account.objects.all()

    return render(request, 'accounts_view.html', {'accounts': accounts})


def create_or_edit_account(request, pk=None):
    """
    Create or edit view that allows us to create
    or edit a account depending if the task list ID
    is null or not
    """
    account = get_object_or_404(Account, pk=pk) if pk else None
    if request.method == 'POST':
        data = request.POST.copy()
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('accounts_view')
    else:
        form = AccountForm(instance=account)
    return render(request, 'accounts_new_form.html', {'form': form})


def delete_account(request, id):
    """
    Deletes the selected account
    """
    account = Account.objects.get(pk=id)
    account.delete()

    return redirect('accounts_view')


def view_detailed_account(request, id):
    """
    a detailed view of an account showing transcations
    """

    account = Account.objects.get(pk=id)
    transcations = Transcation.objects.filter(account=id).order_by('date')

    return render(request, 'accounts_detailed_view.html', {'account': account, 'transcations': transcations})


def update_balance_account(request, id):
    """
    a view that updates the balance of the selected account
    """
    # Incoming values
    total_wages = Transcation.objects.exclude(status='Planned').filter(account=id, type=1).values_list('value').aggregate(Sum('value'))
    if total_wages["value__sum"] == None:
        total_wages["value__sum"] = 0
    total_extraincome = Transcation.objects.exclude(status='Planned').filter(account=id, type=3).values_list('value').aggregate(Sum('value'))
    if total_extraincome["value__sum"] == None:
        total_extraincome["value__sum"] = 0

    total_in = total_wages["value__sum"] + total_extraincome["value__sum"]

    # Outgoing values
    total_expenses = Transcation.objects.exclude(status='Planned').filter(account=id, type=2).values_list('value').aggregate(Sum('value'))
    if total_expenses["value__sum"] == None:
        total_expenses["value__sum"] = 0

    total_bills = Transcation.objects.exclude(status='Planned').filter(account=id, type=4).values_list('value').aggregate(Sum('value'))
    if total_bills["value__sum"] == None:
        total_bills["value__sum"] = 0

    total_out = total_expenses["value__sum"] + total_bills["value__sum"]

    new_balance = total_in - total_out

    account = Account.objects.get(pk=id)
    account.balance = new_balance
    account.save()

    return redirect('view_detailed_account', id)


def periods_view(request):
    periods = Period.objects.all()

    return render(request, 'periods_view.html', {'periods': periods})