from django.shortcuts import render, redirect
from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm
from django.contrib.auth.decorators import login_required


@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Set the user for the transaction
            form.instance.user = request.user
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "add_transaction.html", {"form": form})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, "transaction_list.html", {"transactions": transactions})


@login_required
def set_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            # Associate the budget with the currently logged-in user
            form.instance.user = request.user
            form.save()
            return redirect(
                "set_budget"
            )  # Redirect to the budget list page or any other appropriate page
    else:
        form = BudgetForm()

    return render(request, "set_budget.html", {"form": form})
