from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            var1 = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('sheet:ledger_sheet')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})
