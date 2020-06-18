from django.shortcuts import render, redirect

# Create your views here.
from .models import NewsLetter, Contact, Temoignage, About
from service.models import Service, Project, Apartment
from blog.models import Article

from .forms import ContactForm



def home(request):
    about = About.objects.filter(status=True)
    services = Service.objects.filter(status=True)
    apartments = Apartment.objects.filter(status=True)
    projects = Project.objects.filter(status=True)
    articles = Article.objects.filter(status=True, cathegorie_id=7).order_by('date_update')
    
    data = {
        'about': about.last,
        'services': services,
        'apartments': apartments.order_by('date_update'),
        'projects': projects,
        'recent_apart_articles': articles[:3],
    }
    
    return render(request, 'pages/website/index.html', data)


def about(request):
    about = About.objects.filter(status=True)
    temoignages = Temoignage.objects.filter(status=True)
    apartments = Apartment.objects.filter(status=True)
    
    data = {
        'about': about.last,
        'temoignages': temoignages,
        'apartments': apartments.order_by('date_update'),
    }
    
    return render(request, 'pages/website/about.html', data)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    
    data = {
        'contact_form': contact_form
    }
    
    return render(request, 'pages/website/contact.html', data)


def newsletter(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            new_email = NewsLetter.objects.create(email=email)
            new_email.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
