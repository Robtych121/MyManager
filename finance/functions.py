from .models import Account, Period, Transcation
from django.db.models import Sum

def update_account_bal_from_function(id):
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

    return new_balance


def update_period_bal_from_function(id):
    # Incoming values
    total_wages = Transcation.objects.exclude(status='Planned').filter(period=id, type=1).values_list('value').aggregate(Sum('value'))
    if total_wages["value__sum"] == None:
        total_wages["value__sum"] = 0
    total_extraincome = Transcation.objects.exclude(status='Planned').filter(period=id, type=3).values_list('value').aggregate(Sum('value'))
    if total_extraincome["value__sum"] == None:
        total_extraincome["value__sum"] = 0

    total_in = total_wages["value__sum"] + total_extraincome["value__sum"]

    # Outgoing values
    total_expenses = Transcation.objects.exclude(status='Planned').filter(period=id, type=2).values_list('value').aggregate(Sum('value'))
    if total_expenses["value__sum"] == None:
        total_expenses["value__sum"] = 0

    total_bills = Transcation.objects.exclude(status='Planned').filter(period=id, type=4).values_list('value').aggregate(Sum('value'))
    if total_bills["value__sum"] == None:
        total_bills["value__sum"] = 0

    total_out = total_expenses["value__sum"] + total_bills["value__sum"]

    new_balance = total_in - total_out

    return new_balance


def update_period_totalin_from_function(id):
    # Incoming values
    total_wages = Transcation.objects.exclude(status='Planned').filter(period=id, type=1).values_list('value').aggregate(Sum('value'))
    if total_wages["value__sum"] == None:
        total_wages["value__sum"] = 0
    total_extraincome = Transcation.objects.exclude(status='Planned').filter(period=id, type=3).values_list('value').aggregate(Sum('value'))
    if total_extraincome["value__sum"] == None:
        total_extraincome["value__sum"] = 0

    total_in = total_wages["value__sum"] + total_extraincome["value__sum"]

    return total_in


def update_period_totalout_from_function(id):
    # Outgoing values
    total_expenses = Transcation.objects.exclude(status='Planned').filter(period=id, type=2).values_list('value').aggregate(Sum('value'))
    if total_expenses["value__sum"] == None:
        total_expenses["value__sum"] = 0

    total_bills = Transcation.objects.exclude(status='Planned').filter(period=id, type=4).values_list('value').aggregate(Sum('value'))
    if total_bills["value__sum"] == None:
        total_bills["value__sum"] = 0

    total_out = total_expenses["value__sum"] + total_bills["value__sum"]

    return total_out