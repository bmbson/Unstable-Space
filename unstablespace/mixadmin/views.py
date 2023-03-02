from django.shortcuts import HttpResponse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MixModel
from .forms import Mix, Login


def mixadminlogin(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'mixadmin/mixadminfront.html')
            else:
                form = Login()
                messages.add_message(request, messages.ERROR, 'Wrong Username or Password.')
                return render(request, 'mixadmin/mixadminlogin.html', {'form': form})
        else:
            form = Login()
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'mixadmin/mixadminlogin.html', {'form': form})

    else:
        form = Login()

    return render(request, 'mixadmin/mixadminlogin.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect(mixadminlogin)

@login_required
def mixadminfront(request):
    return render(request, 'mixadmin/mixadminfront.html')

@login_required
def createmix(request):
    if request.method == "POST":
        form = Mix(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            image = request.FILES['image']
            creator = request.POST.get('creator')
            backgroundImg = request.FILES['backgroundImg']
            audio = request.FILES['audio']
            tag = request.POST.get('tag')
            tag2 = request.POST.get('tag2')
            description = request.POST.get('description')
            mix = MixModel.objects.create(title=title, image=image, audio=audio, creator=creator,
                                           backgroundImg=backgroundImg, tag=tag, tag2=tag2,
                                           description=description)
            mix.save()
            return HttpResponse("Mix {} uploaded".format(str(mix.title)))

    else:
        form = Mix()
    return render(request, 'mixadmin/createmix.html', {'form': form})

@login_required
def deletemix(request):
    return render(request, 'mixadmin/deletemix.html')

@login_required
def updatemix(request):
    return render(request, 'mixadmin/updatemix.html')

@login_required
def uploadcomplete(request):
    return render(request, 'mixadmin/uploadcomplete.html')
