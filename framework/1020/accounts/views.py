from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users" : users,
    }
    return render(request, 'accounts/index.html', context)

from .forms import CustomUserCreationForm 

def signup(request):
    signup_form = CustomUserCreationForm()
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    context = {
        'signup_form': signup_form
    }
    return render(request, 'accounts/form.html', context)

from .forms import CustomUserChangeForm

@login_required
def update(request, user_pk):
    update_form = CustomUserChangeForm(instance=request.user)
    if request.method == "POST":
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('accounts:index')
    context = {
        'signup_form': update_form
    }
    return render(request, 'accounts/form.html', context)



from django.contrib.auth.forms import AuthenticationForm

def login(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('accounts:index')
    context = {
        "login_form" : login_form
    }
    return render(request, 'accounts/login.html', context)

from django.contrib.auth import logout as auth_logout

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def profile(request, user_pk):
    return render(request, 'accounts/profile.html')

from django.contrib.auth.forms import PasswordChangeForm

def change_password(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    change_password_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        change_password_form = PasswordChangeForm(request.user, request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            return redirect('accounts:profile', user.pk)
    context = {
        "change_password_form" : change_password_form,
    }
    return render(request, 'accounts/change_password.html', context)
    
