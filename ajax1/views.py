from itertools import tee
import re
from django.http import JsonResponse
from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse, HttpResponse
from .forms import PhotoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getProfiles(request):
        profiles = Profile.objects.all()

        return JsonResponse({'profiles':list(profiles.values())})

def Form(request):
    return render(request, 'form.html')       

def Create(request):

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']     

        new_profile = Profile(name=name, email=email, bio=bio)

        new_profile.save()

        return HttpResponse('User Created Successfully')

#This is ajax and forms.py together

def AjaxForm(request):

    form = PhotoForm(request.POST or None, request.FILES or None)
    data ={}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {
        'form':form
    }

    return render(request, 'main.html',context)        