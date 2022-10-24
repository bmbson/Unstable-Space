from cgitb import html
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Mix

# Create your views here.
def mixadminfront(request):
    return render(request, 'mixadmin/mixadminfront.html')

def createmix(request):
    if request.method == "POST":
        form = Mix(request.POST, request.FILES)
        if form.is_valid():
             return render(request, 'mixadmin/uploadcomplete.html')

    else:
        form = Mix()
    return render(request, 'mixadmin/createmix.html', {'form': form})

def deletemix(request):
    return render(request, 'mixadmin/deletemix.html')

def updatemix(request):
    return render(request, 'mixadmin/updatemix.html')

def uploadcomplete(request):
    return render(request, 'mixadmin/uploadcomplete.html')