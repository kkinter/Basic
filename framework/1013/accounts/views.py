from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm
from accounts.models import Users
# Create your views here.
def index(request):
    users = Users.objects.all()
    msg = 'HI'
    if not request.user.is_authenticated:
        msg = 'Hi, Anonymous User'
    else:
        msg = f'Hi, {request.user}'
    

    context = {
        'users': users,
        'msg' : msg
    }
    return render(request, 'accounts/index.html', context)

from django.contrib.auth import get_user_model

def signup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, user_pk):
    user = Users.objects.get(pk=user_pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/detail.html', context)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserChangeForm

@login_required
def update(request, pk):
    user_id = request.user.id

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        'user_id' : user_id,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) 

    return redirect('accounts:index')

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def update_password(request, pk) :
    user_id = request.user.id
    
    if request.method == "POST" :
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid() :
            user = form.save() # 이때 로그아웃처리됨. session 정보 날라가고, 로그인정보도 사라짐
            update_session_auth_hash(request, user) # session 을 update 이렇게 해야 비밀번호를 바꾸더라도 로그아웃이 되지 않음
            return redirect('accounts:index')
    else :
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
        'user_id': user_id
    }
    return render(request, 'accounts/update_password.html', context)
