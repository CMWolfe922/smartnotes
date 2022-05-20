from django.db import models

# import the generic User object
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)