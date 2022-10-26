from django.db import models

# Create your models here.
class MixModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField()
    audio = models.FileField()
    tag = models.CharField(max_length=20)