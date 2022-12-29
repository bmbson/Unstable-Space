from django.db import models
import os

# Create your models here.
class MixModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    tag = models.CharField(max_length=25, blank=True)
    tag2 = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
