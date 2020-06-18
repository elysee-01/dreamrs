from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    photo = models.ImageField(upload_to="images/PhotoProfile")
    adresse = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
