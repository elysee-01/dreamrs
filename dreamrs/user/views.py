from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .forms import LoginForm, RegisterForm



def register_view(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('login')
    else:
        form = RegisterForm()
    
    data = {
        'form': form
    }
    
    return render(request, 'pages/user/register.html', data)



def login_view(request):
    
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



def logout_view(request):
    logout(request)
    return redirect('login')