from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from .forms import MyUserCreationForm

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            raise ObjectDoesNotExist("User is not found")
    context = {

    }
    return render(request, 'auth/login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('auth:login')
    return render(request, 'auth/logout.html')


def register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    context = {
        "form": form
    }
    return render(request, 'auth/register.html', context)
