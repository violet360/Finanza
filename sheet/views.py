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
    
    
    users = User.objects.all()
    print(users)
    for i in Group.objects.all():
        print(i.pk, "--------")

    auth_user = request.user.username

    profit = 0.0

    Parts = []
    ledgers = Ledger.objects.all()

    grps = []

    for transaction in ledgers:
        print(transaction.pk,"  ", transaction.lender, "   00000000000")

        if(transaction.lender == auth_user):
            if(transaction.grp not in Parts):
                Parts.append(transaction.grp)

            profit+=transaction.amount
            

        if(transaction.borrower == auth_user):
            if(transaction.grp not in Parts):
                Parts.append(transaction.grp)

            profit-=transaction.amount

    ledgers = []


    for p in Parts:
        print(p)
        obj = Group.objects.get(grp_name = p)
        grps.append(obj)

        pks = json.loads(obj.pk_vals)

        for Pk in pks:
            ledgers.append(Ledger.objects.get(pk = Pk))


    return render(request,'sheet/ledger.html',{'form': form, 'ledgers': ledgers, 'users':users, 'money':profit, 'parts':Parts, 'grps':grps})


@login_required
def grp_view(request, pk):
    obj = Group.objects.get(pk = pk)
    print(obj.grp_name)
    pks = json.loads(obj.pk_vals)
    ans = []
    for i in pks:
        print(i, "++++")
        ans.append(Ledger.objects.get(pk = i))

    return render(request, 'sheet/grp.html', {'transactions':ans})


@login_required
def transaction_del(request, pk):
    obj = Ledger.objects.get(pk = pk)
    var1 = Group.objects.get(grp_name = obj.grp)

    pks = json.loads(var1.pk_vals)
    print(pk, "----", pks, type(pks))

    pks.remove(pk)
    

    print(pks, type(pks), pk)
    var1.pk_vals = json.dumps(pks)
    var1.save()


    print(var1.pk_vals)

    obj.delete()

    return redirect('sheet:ledger_sheet')



@login_required
def go(request, pk):
    obj = Ledger.objects.get(pk = pk)
    return render(request, 'sheet/yousure.html', {'obj':obj})
