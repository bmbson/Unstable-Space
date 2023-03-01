from django.shortcuts import render
from mixadmin.models import MixModel
from mixadmin.models import TrackToMix
from mixadmin.models import Track
from django.shortcuts import get_object_or_404
from django.db.models import Q

def frontPage(request):
    return render(request, 'main/frontPage.html')

def contact(request):
    return render(request, 'main/contact.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def secret(request):
    return render(request, 'main/secret.html')

def mixes(request):
    tag1 = MixModel.objects.values('tag').distinct()
    tag2 = MixModel.objects.values('tag2').distinct()

    tagList = tag1.union(tag2)
    if request.method == 'GET':
        context = {'MixModel':MixModel.objects.all(), 'genreList':tagList}

    elif request.method == 'POST':
        tag = request.POST.get('genre')
        title = "" if request.POST.get('search') == None else request.POST.get('search')
       
        order = "created_at"

        if request.POST.get('selectBy') == 'oldest':
            order = "-created_at"

        if tag == "" and title == "":
            context = {'MixModel':MixModel.objects.all().order_by(order), 'genreList':tagList}
        elif tag == "":
            context = {'MixModel':MixModel.objects.filter(title__contains=title).order_by(order), 'genreList':tagList}
        elif title == "":
            if tag2 == None:
                context = {'MixModel':MixModel.objects.filter(tag=tag).order_by(order), 'genreList':tagList}
            else:
                context = {'MixModel':MixModel.objects.filter(Q(tag=tag) | Q(tag2=tag)).order_by(order), 'genreList':tagList}
        else:
            context = {'MixModel':MixModel.objects.filter(title__contains=title).filter(Q(tag=tag) | Q(tag2=tag)).order_by(order), 'genreList':tagList}

    return render(request, 'main/mixes.html', context)

def tagClicked(request):
    tag1 = MixModel.objects.values('tag').distinct()
    tag2 = MixModel.objects.values('tag2').distinct()

    tagList = tag1.union(tag2)


    return render(request, 'main/mixes.html', context)

def about(request):
    return render(request, 'main/about.html')

def merch(request):
    return render(request, 'main/merch.html')

def blog(request):
    return render(request, 'main/blog.html')

def privacyPolicy(request):
    return render(request, 'main/privacypolicy.html')

def individualMix(request, mixName):
    reqMixModel = get_object_or_404(MixModel, title=mixName)
    
    trackList = Track.objects.filter(tracktomix__playlistId=reqMixModel.pk)
    context = {'MixModel':reqMixModel, 'trackList':trackList}
    return render(request, 'main/individualmix.html', context)
    
