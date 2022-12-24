from django.shortcuts import render
from mixadmin.models import MixModel

def frontPage(request):
    return render(request, 'main/frontPage.html')

def contact(request):
    return render(request, 'main/contact.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def secret(request):
    return render(request, 'main/secret.html')

def mixes(request):
    context = {'MixModel':MixModel.objects.all()}
    return render(request, 'main/mixes.html', context)

def about(request):
    return render(request, 'main/about.html')

def merch(request):
    return render(request, 'main/merch.html')

def blog(request):
    return render(request, 'main/blog.html')

def privacypolicy(request):
    return render(request, 'main/privacypolicy.html')
