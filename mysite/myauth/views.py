from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm

def my_login(request):
    redirect_url = reverse("main")
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'myauth/login.html')
        return redirect(redirect_url)

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'myauth/login.html', {"error": "Пользователь не найден"})

def profile(request):
    return render(request, 'myauth/profile.html')

def my_logout(request):
    login_url = reverse("login")
    logout(request)
    return redirect(login_url)

def register(request):
    print(request.POST)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'myauth/register.html', context)
