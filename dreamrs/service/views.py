from django.shortcuts import render

# Create your views here.
from website.models import Temoignage, About
from .models import Service, Apartment, Project

def service(request):
    about = About.objects.filter(status=True)
    services = Service.objects.filter(status=True)
    temoignages = Temoignage.objects.filter(status=True)
    
    data = {
        'about': about.last,
        'services': services,
        'temoignages': temoignages,
    }
    
    return render(request, 'pages/service/services.html', data)


def apartment(request):
    apartments = Apartment.objects.filter(status=True)
    
    data = {
        'apartments': apartments.order_by('date_update'),
        'apartment_detail': apartments.order_by('id').last,
    }
    
    return render(request, 'pages/service/apartment.html', data)


def project(request):
    projects = Project.objects.filter(status=True)
    
    data = {
        'projects': projects,
    }
    
    return render(request, 'pages/service/project.html', data)