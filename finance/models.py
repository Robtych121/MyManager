from django.db import models


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