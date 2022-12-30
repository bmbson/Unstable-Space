from django import forms

class Mix(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    audio = forms.FileField()
    tag = forms.CharField(max_length=20)

class Login(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)