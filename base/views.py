from cProfile import Profile
from http.client import responses
from urllib import response
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import RForm
from django.contrib import messages
from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        ssu=request.user

    else:
        return redirect('loginr')

    return render(request, 'home.html',{'ssu':ssu})





def register(request):
   
    form = RForm()
    if request.method == 'POST':
        form = RForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginr')
        else:
            return HttpResponse("not working")
               
        
    context={'form':form}
    return render(request, 'loginr.html',context)







def loginr(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        emailw = request.POST.get('email')
        passs = request.POST.get('password') 
        try:
            user = User.objects.get(email=emailw)
            
        except:
            messages.error(request, '{} does not exist'.format(emailw))

        user=authenticate(request, email=emailw, password=passs)   
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username password does not exist')

    
   
    # return render(request,'loginr.html', context)
    
    return render(request, 'login.html')





def logoutUser(request):
    logout(request)
    return redirect('home')


