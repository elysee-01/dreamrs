from django.db import models

# Create your models here.
from dreamrs.settings import AUTH_USER_MODEL


class SiteInfo(models.Model):
    
    name = models.CharField(max_length = 150)
    icon = models.ImageField(upload_to='images/icon')
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length = 150)
    adresse = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Info du site'
        verbose_name_plural = 'Infos du site'

    def __str__(self):
        return self.name



class SocialAccount(models.Model):
    ICONS = [
        ("fab fa-facebook-f", "Facebook"),
        ("fab fa-twitter", "Twitter"),
        ("fas fa-globe", "Globe"),
        ("fab fa-behance", "Behance"),
    ]

    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials accounts'

    def __str__(self):
        return self.nom



class NewsLetter(models.Model):
    email = models.EmailField()
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email



class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length = 150)
    sujet = models.CharField(max_length = 150)
    email = models.EmailField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.nom} : {self.sujet}'



class Temoignage(models.Model):
    nom = models.CharField(max_length = 255, null=True)
    prenom = models.CharField(max_length = 255, null=True)
    message = models.TextField()
    metier = models.CharField(max_length = 150)
    photo = models.ImageField(upload_to='images/Temoignage', null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return f'{self.prenom} {self.nom}'



class About(models.Model):
    
    image = models.ImageField(upload_to='images/About')
    title = models.CharField(max_length = 255)
    description = models.TextField()
    
    service_title = models.CharField(max_length = 255)
    service_description = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.title
