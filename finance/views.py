from django.shortcuts import render
from .models import Account, Period
from .forms import AccountForm

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



def periods_view(request):
    periods = Period.objects.all()

    return render(request, 'periods_view.html', {'periods': periods})