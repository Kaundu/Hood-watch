from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.



class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # occupants = models.IntegerField(null= True,blank=True)
    admin =  models.ForeignKey(User, related_name="made_by", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 )
    last_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    neighbor_hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name="hood", null=True,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True)

    def __str__(self):
        return self.first_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=255, blank=True )
    email = models.CharField(max_length=50)
    owner =  models.ForeignKey(User, related_name="owned_by", on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='posted_by')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='posts_for')

    def __str__(self):
        return self.title