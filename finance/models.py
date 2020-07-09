from django.db import models
from datetime import datetime
import calendar

# Create your models here.
class Account(models.Model):

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    balance = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    currency = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name


class Period(models.Model):
    firstDayOfMonth = datetime.today().replace(day=1)
    now = datetime.now()
    lastDayOfMonth = datetime.today().replace(day=calendar.monthrange(now.year,now.month)[1])


    class Meta:
        verbose_name = 'Period'
        verbose_name_plural = 'Periods'

    name = models.CharField(max_length=254, default='')
    startDate = models.DateField(default=firstDayOfMonth)
    endDate = models.DateField(default=lastDayOfMonth)
    startBalance = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    endBalance = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    totalIn = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    totalOut = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    freeCash = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    STATUSCHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=254, choices=STATUSCHOICES, default='')


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, default='')


class Type(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    name = models.CharField(max_length=254, default='')


class Transcation(models.Model):
    class Meta:
        verbose_name = 'Transcation'
        verbose_name_plural = 'Transcations'


    name = models.CharField(max_length=254, default='')
    value = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    STATUSCHOICES = (
        ('Paid', 'Paid'),
        ('Planned', 'Planned')
    )
    status = models.CharField(max_length=254, choices=STATUSCHOICES, default='')
    notes = models.CharField(max_length=254, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)