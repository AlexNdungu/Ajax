from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(verbose_name='Full Name', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='Email')
    bio = models.TextField(verbose_name='User Bio')

    def __str__(self):
        return str(self.name)

class Photo(models.Model):
    name = models.CharField(max_length=15)
    desciption = models.TextField()
    image = models.ImageField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)  