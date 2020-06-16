from django.shortcuts import render

# Create your views here.


def home(request):
    
    data = {
        
    }
    
    return render(request, 'pages/website/index.html', data)


def about(request):
    
    data = {
        
    }
    
    return render(request, 'pages/website/about.html', data)


def contact(request):
    
    data = {
        
    }
    
    return render(request, 'pages/website/contact.html', data)