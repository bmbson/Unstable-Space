from django.db import models
import os

# Create your models here.
class MixModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    creator = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    tag = models.CharField(max_length=25, blank=True)
    tag2 = models.CharField(max_length=25, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Track(models.Model):
    trackTitle = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)

class TrackToMix(models.Model):
    playlistId = models.ForeignKey(MixModel, on_delete=models.CASCADE)
    trackId = models.ForeignKey(Track, on_delete=models.CASCADE)
    position = models.IntegerField()