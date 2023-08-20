# transactions/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("add_transaction/", views.add_transaction, name="add_transaction"),
    path("transaction_list/", views.transaction_list, name="transaction_list"),
    path("set_budget/", views.set_budget, name="set_budget"),
    # Define URLs for budget management, report generation, and transaction visualization.
]
