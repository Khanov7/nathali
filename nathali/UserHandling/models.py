from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Device(models.Model):
    device_name = models.CharField(max_length=100)


class UserProfile(AbstractUser):

    USER_STATUS = (
        ("Approved", "Approved"),
        ("pending", "pending")
    )
    first_name = models.CharField(max_length=30, help_text='Enter first name')
    last_name = models.CharField(max_length=50, help_text='Enter Last name')
    profilePicture = models.FileField(verbose_name='profile picture', upload_to='Profile Pictures')
    status = models.CharField(choices=USER_STATUS,max_length=50)
    birthday = models.DateField()
    occupation = models.CharField(max_length=30, default="")
    country = models.CharField(default="",max_length=50)
    city = models.CharField(default="",max_length=50)