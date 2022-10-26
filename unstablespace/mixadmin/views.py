from django.shortcuts import HttpResponse, render
from .models import MixModel
from .forms import Mix

# Create your views here.
def mixadminfront(request):
    return render(request, 'mixadmin/mixadminfront.html')

def createmix(request):
    if request.method == "POST":
        form = Mix(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            image = request.POST.get('image')
            audio = request.POST.get('audio')
            tag = request.POST.get('tag')

            mix = MixModel.objects.create(title=title, image=image, audio=audio, tag=tag)
            mix.save()
            return HttpResponse("Mix {} uploaded".format(str(mix.title)))

    else:
        form = Mix()
    return render(request, 'mixadmin/createmix.html', {'form': form})

def deletemix(request):
    return render(request, 'mixadmin/deletemix.html')

def updatemix(request):
    return render(request, 'mixadmin/updatemix.html')

def uploadcomplete(request):
    return render(request, 'mixadmin/uploadcomplete.html')