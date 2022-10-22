from django.shortcuts import render

# Create your views here.
def mixadminfront(request):
    return render(request, 'mixadmin/mixadminfront.html')

def createmix(request):
    return render(request, 'mixadmin/createmix.html')

def deletemix(request):
    return render(request, 'mixadmin/deletemix.html')

def updatemix(request):
    return render(request, 'mixadmin/updatemix.html')

    