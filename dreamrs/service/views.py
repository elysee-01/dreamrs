from django.shortcuts import render

# Create your views here.


def service(request):
    
    data = {
        
    }
    
    return render(request, 'pages/service/services.html', data)


def apartment(request):
    
    data = {
        
    }
    
    return render(request, 'pages/service/apartment.html', data)


def project(request):
    
    data = {
        
    }
    
    return render(request, 'pages/service/project.html', data)