from django.contrib import admin
from .models import Account, Period, Category, Type, Transcation

# Register your models here.
admin.site.register(Account)
admin.site.register(Period)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Transcation)