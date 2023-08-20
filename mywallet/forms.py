# transactions/forms.py

from django import forms
from .models import Transaction, Budget


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["account", "category", "amount", "date", "description"]


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["limit"]
