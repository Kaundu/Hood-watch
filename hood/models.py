from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50 )
    last_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin =  models.ForeignKey(User, related_name="made_by", on_delete=models.CASCADE)
