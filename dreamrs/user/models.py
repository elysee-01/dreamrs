from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    photo = models.ImageField(upload_to="images/PhotoProfile")
    adresse = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)



