from django.db import models
from django.contrib.auth.models import AbstractUser


class Projects(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class Users(AbstractUser):
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name
