from django.db import models

# Create your models here.

class Service(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Service', blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom



class ProjectType(models.Model):
    name = models.CharField(max_length = 255)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Project type'
        verbose_name_plural = 'Projects types'

    def __str__(self):
        return self.name



class Project(models.Model):
    type_projet = models.ForeignKey(ProjectType, on_delete=models.CASCADE, related_name='project_type')
    image = models.ImageField(upload_to='images')
    titre = models.CharField(max_length = 255)
    nouveau_projet = models.BooleanField(default=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.titre


class Apartment(models.Model):
    type_apart = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='images/Apartment')
    description = models.TextField()
    nombre_salle_bain = models.PositiveIntegerField()
    nombre_chambre = models.PositiveIntegerField()
    nombre_fenetre = models.PositiveIntegerField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'

    def __str__(self):
        return self.type_apart
