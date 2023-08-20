from django.contrib import admin

# Register your models here.
# transactions/admin.py

from django.contrib import admin
from .models import Account, Category, Subcategory, Transaction, Budget

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transaction)
admin.site.register(Budget)
