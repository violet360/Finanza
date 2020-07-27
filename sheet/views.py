from django.shortcuts import render, redirect
from .models import Ledger
from .forms import LedgerForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sheet.models import Ledger

@login_required
def ledger_view(request):
    if request.method =='POST':
        form = LedgerForm(request.POST)

        if form.is_valid():
            ledger = form.save(commit=False)
            ledger.save()

            form = LedgerForm()
            return redirect('sheet:ledger_sheet')

    else:
        form = LedgerForm()
    
    ledgers = Ledger.objects.all()
    users = User.objects.all()

    auth_user = request.user.username

    profit = 0.0

    for transaction in ledgers:
        if(transaction.lender == auth_user):
            profit+=transaction.amount

        elif(transaction.borrower == auth_user):
            profit-=transaction.amount        



    return render(request,'sheet/ledger.html',{'form': form, 'ledgers': ledgers, 'users':users, 'money':profit})