from django.contrib import admin

# Register your models here.
from .models import MixModel
from .models import Track
from .models import TrackToMix

admin.site.register(Track)
admin.site.register(MixModel)
admin.site.register(TrackToMix)