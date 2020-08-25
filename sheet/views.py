from django.shortcuts import render, redirect, HttpResponse
from .models import Ledger, Group
from .forms import LedgerForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sheet.models import Ledger
import json

@login_required
def ledger_view(request):
    if request.method =='POST':
        form = LedgerForm(request.POST)

        if form.is_valid():
            ledger = form.save(commit=False)

            ledger.save()

            print(ledger.pk, "---------")
            print(ledger.grp, "---------------------------------------")

            if not Group.objects.filter(grp_name=ledger.grp).exists():
                Group.objects.create(grp_name = ledger.grp)
            var = Group.objects.get(grp_name = ledger.grp)
            e = json.loads(var.pk_vals)
            e.append(ledger.pk)
            var.pk_vals = json.dumps(e)
            var.save()

            form = LedgerForm()
            return redirect('sheet:ledger_sheet')

    else:
        form = LedgerForm()
    
    ledgers = Ledger.objects.all()
    users = User.objects.all()
    print(users)
    for i in Group.objects.all():
        print(i.pk, "--------")

    auth_user = request.user.username

    profit = 0.0

    Parts = []

    grps = Group.objects.all();

    for transaction in ledgers:
        print(transaction.pk)

        if(transaction.grp not in Parts):
                Parts.append(transaction.grp)

        if(transaction.lender == auth_user):
            profit+=transaction.amount
            

        if(transaction.borrower == auth_user):
            profit-=transaction.amount




    return render(request,'sheet/ledger.html',{'form': form, 'ledgers': ledgers, 'users':users, 'money':profit, 'parts':Parts, 'grps':grps})



def grp_view(request, pk):
    obj = Group.objects.get(pk = pk)
    print(obj.grp_name)
    pks = json.loads(obj.pk_vals)
    ans = []
    for i in pks:
        print(i, "++++")
        ans.append(Ledger.objects.get(pk = i))

    return render(request, 'sheet/grp.html', {'transactions':ans})
