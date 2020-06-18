from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from .forms import LoginForm


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)
    
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    data = {
        'form': form,
    }
    
    return render(request, 'pages/user/login.html', data)



def logout_page(request):
    logout(request)
    return redirect('login')