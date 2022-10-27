from email.mime import image
from site import abs_paths
from django.db import models
import os

# Create your models here.
class MixModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    tag = models.CharField(max_length=50)
    
