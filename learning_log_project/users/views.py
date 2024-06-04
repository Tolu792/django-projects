from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from learning_logs.views import main

from django.contrib.auth.models import auth, Group
from django.contrib.auth import authenticate


# Create your views here.
def register(request):
    """function to register new users."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'registerform': form}
    return render(request, 'register.html', context=context)


def login(request):
    """function to log in registered users"""
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('learning_logs:main')
    context = {'loginform': form}
    return render(request, 'login.html', context=context)


def user_logout(request):
    """function to log out registered users"""
    auth.logout(request)
    return redirect('learning_logs:main')
