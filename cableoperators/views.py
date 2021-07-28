from django.shortcuts import render,redirect
from .models import SitiNetwork
from .forms import SitiNetworkForm
from django.views import View
from django.contrib.auth import authenticate, logout




def index(request):
    amplifiers=SitiNetwork.objects.all()
    return render(request,'index.html',{'amplifiers':amplifiers})


def create(request):
    if request.method == 'POST':
        print(request.POST)
        form = SitiNetworkForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/cableoperators/index/')
    else:
        form = SitiNetworkForm()
    return render(request, 'create.html', {'form': form})


def edit(request, sitiid):
    amplifiers = SitiNetwork.objects.get(sitiid=sitiid)
    form = SitiNetworkForm(instance=amplifiers)
    return render(request, 'update.html', {'form': form, 'sitiid': sitiid})


def update(request, sitiid):
    amplifiers = SitiNetwork.objects.get(sitiid=sitiid)
    form = SitiNetworkForm(request.POST, instance=amplifiers)
    if form.is_valid():
        form.save()
        return redirect('/amplifiers/update/')
    return render(request, 'update.html', {'form': form, 'sitiid': sitiid})



def delete(request, sitiid):
    amplifiers = SitiNetwork.objects.get(sitiid=sitiid)
    print('amplifiers', amplifiers)
    amplifiers.delete()
    return redirect('/cableoperators/index/')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        print(user)
        if user:
            return redirect('/cableoperators/index/')
    return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('/cableoperators/login/')
# Create your views here.
