from django.shortcuts import render, redirect
## 회원가입
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User
## 로그인
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
# Create your views here.
## login required
## @login_required(login_url="login") 페이지 권한?
from django.contrib.auth.decorators import login_required

## 메세지
from django.contrib import messages

def loginPage(request):

    # if request.user.is_authenticated:
    #     return redirect('profiles')


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)

        try:
            user = User.objects.get(username=username)
        except:
            print('Username이 존재하지 않습니다.')
            messages.error(request, 'Username이 존재하지 않습니다.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:index')
        else:
            messages.error(request, 'Username 혹은 비밀번호가 올바르지 않습니다.')

    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('accounts:index')

def index(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    
    context = {
        "form" : form
    }

    return render(request, 'accounts/signup.html', context)

@login_required(login_url="accounts:login") 
def detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request, 'accounts/detail.html', context)

