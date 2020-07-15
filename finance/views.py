from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Period, Transcation
from .forms import AccountForm
from django.db.models import Sum
from .functions import update_account_bal_from_function

# Create your views here.
def homepage(request):
    return render(request, 'financehome.html')


def accounts_view(request):
    accounts = Account.objects.all()
    
    for account in accounts:
        acc_id = int(account.id)
        update_account = Account.objects.get(pk=acc_id)
        update_account.balance = update_account_bal_from_function(acc_id)
        update_account.save()

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
    account = Account.objects.get(pk=id)
    account.balance = update_account_bal_from_function(id)
    account.save()

    return redirect('view_detailed_account', id)


def periods_view(request):
    periods = Period.objects.all()

    return render(request, 'periods_view.html', {'periods': periods})