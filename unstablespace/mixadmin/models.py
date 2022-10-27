from django.db import models

# Create your models here.
class MixModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    audio = models.FileField(upload_to='uploads/')
    tag = models.CharField(max_length=20)