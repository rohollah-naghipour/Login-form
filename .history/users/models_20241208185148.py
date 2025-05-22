from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length= 150, null = False, unique= True)
    password = models.CharField(max_length = 15, unique = True, null = False)
    email = models.EmailField(max_length= 250)


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 165, null=True, unique=False)
    last_name = models.CharField(max_length=140, null= True, unique= False)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
        
