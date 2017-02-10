from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userOBJ(models.Model):
    contacts = models.CharField(max_length=11,null=True, blank=True)
    user = models.OneToOneField(User, unique=True, primary_key=True)
    objects = models.Manager()