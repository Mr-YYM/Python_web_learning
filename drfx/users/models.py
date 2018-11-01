from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email
    

