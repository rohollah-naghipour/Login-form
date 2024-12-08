from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length= 150, null = False)
    name = models.CharField(max_length= 100, null = True)
    password = models.CharField(max_length = 15, unique = True, null = False)
    email = models.EmailField(max_length= 250)
