from unittest.util import _MAX_LENGTH
from django.db import forms

class Mix(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.FileField()
    audio = forms.FileField()
    tags = forms.CharField(max_length=20)

