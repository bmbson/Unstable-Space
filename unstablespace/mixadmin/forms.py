from distutils.command.upload import upload
from django import forms

class Mix(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.FileField(required=False)
    audio = forms.FileField(required=False)
    tag = forms.CharField(max_length=20)