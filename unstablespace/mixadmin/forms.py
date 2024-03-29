from django import forms

class Mix(forms.Form):
    title = forms.CharField(max_length=50)
    creator = forms.CharField(max_length=50)
    image = forms.ImageField()
    backgroundImg = forms.ImageField()
    audio = forms.FileField()
    tag = forms.CharField(max_length=20)
    tag2 = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"4"}))
    

class Login(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)