from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Users
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    users = Users.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def create(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    context = {
        'form' : form
    }
    return render(request, 'accounts/create.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, '로그인 하였습니다.')
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)    

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('accounts:index')

@login_required
def detail(requset,pk):
    user = Users.objects.get(pk=pk)
    context = {
        "user" : user
    }
    return render(requset, 'accounts/detail.html', context)

@login_required
def update(request, pk):
    user = Users.objects.get(pk=pk)
    form = CustomUserChangeForm(instance=user)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    context = {
        'user' : user,
        'form' : form,
    }
    return render(request, 'accounts/create.html', context)
@login_required
def delete(request, pk):
    user = Users.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('accounts:index')
    return render(request, 'accounts/delete.html')


from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)