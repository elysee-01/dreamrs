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
        ("ti-facebook", "Facebook"),
        ("fa-twitter", "Twitter"),
        ("fa-google-plus", "Google +"),
        ("fa-linkedin", "Linkedin"),
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
    auteur = models.ForeignKey(AUTH_USER_MODEL, related_name='auteur_temoignage', on_delete=models.CASCADE)
    message = models.TextField()
    metier = models.CharField(max_length = 150)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return str(self.auteur)
