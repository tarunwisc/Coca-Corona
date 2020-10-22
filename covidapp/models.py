from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    status= models.BooleanField(default=False)
    