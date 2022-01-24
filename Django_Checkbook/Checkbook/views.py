from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.urls import reverse

from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

# Create your views here.
def checkbook(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balanceSheet(request, pk)
    content = { 'form': form }
    return render(request, "checkbook/index.html", content)

def newAccount(request):
    return render(request, "checkbook/CreateNewAccount.html")

def balanceSheet(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = { }
    for t in transactions:
        if t.type == 'deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    content = { 'account': account, 'table_contents': table_contents, 'balance': current_total }
    return render(request, 'checkbook/BalanceSheet.html', content)

def addTransaction(request):
    return render(request, "checkbook/AddTransaction.html")


def create_account(request):
     form = AccountForm(data=request.POST or None)
     if request.method == 'POST':
         if form.is_valid():
             form.save()
             return redirect('home')
     content = { 'form': form }
     return render(request, 'checkbook/CreateNewAccount.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']

            form.save()
            # I really don't like this, however the alternate option would continue to resubmit the form upon refresh
            return HttpResponseRedirect("../{}/balance/".format(pk))
    content = { 'form': form }
    return render(request, 'checkbook/AddTransaction.html', content)



