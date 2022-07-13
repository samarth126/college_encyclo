from cProfile import Profile
from http.client import responses
from re import M
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
from .forms import RForm,Form2
from django.contrib import messages
from django.shortcuts import render
from .models import Events,Profile,College

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        ssu = request.user
        pro, created = Profile.objects.get_or_create(user = ssu)
        sad, created1 = Staffadmin.objects.get_or_create(user = ssu)
        staf=ssu.staff
        if(staf == 'N'):
            if(pro.detail_filled == False):
                return redirect('proform')
            # else:
            #     return redirect('home')
        else:
            if(sad.detail_filled_s == False):
                return redirect('staffproform')
            # else:
            #     return redirect('home')
    else:
        return redirect('logins')

    return render(request, 'home.html',{'ssu':ssu})


def proform(request):
    if request.user.is_authenticated:
        ssu=request.user
        pro = Profile.objects.get(user=ssu)
        if(pro.detail_filled == True):
            return redirect('home')
        c=College.objects.all()
        p=Program.objects.all()
        d=Department.objects.all()
        y=Year.objects.all()
        # form2 = Form2()
        if request.method == "POST":
            college = request.POST.get('cllg')
            program = request.POST.get('prog')
            department = request.POST.get('dept')
            year = request.POST.get('yer')
            v = College.objects.get(id=college)
            x = Program.objects.get(id=program)
            y = Department.objects.get(id=department)
            z = Year.objects.get(id=year)
            gen = request.POST.get('gender')
            pro.college = v
            pro.program = x
            pro.department = y
            pro.year = z
            pro.gender = gen
            pro.detail_filled = True
            pro.save()
                # messages.success(request, 'Your account has been created successfully!')

        context={'c':c, 'p':p, 'd':d, 'y':y}
        return render(request, 'proform.html', context)

def staffproform(request):
        if request.user.is_authenticated:
            ssu=request.user
            sad = Staffadmin.objects.get(user=ssu)
            if(sad.detail_filled_s == True):
                return redirect('home')
            c=College.objects.all()
            p=Program.objects.all()
            d=Department.objects.all()
            y=Year.objects.all()
            cb=Club.objects.all()
            if request.method == "POST":
                college = request.POST.get('cllg')
                program = request.POST.get('prog')
                department = request.POST.get('dept')
                year = request.POST.get('yer')
                club = request.POST.get('clb')
                v = College.objects.get(id=college)
                x = Program.objects.get(id=program)
                y = Department.objects.get(id=department)
                z = Year.objects.get(id=year)
                gen = request.POST.get('gender')
                t= Club.objects.get(id=club)
                sad.college = v
                sad.program = x
                sad.department = y
                sad.year = z
                sad.gender = gen
                sad.club = t
                sad.detail_filled_s = True
                sad.save()
                # messages.success(request, 'Your account has been created successfully!')

            context={'c':c, 'p':p, 'd':d, 'y':y, 'cb':cb}
            return render(request, 'staffproform.html', context)

def register(request):
   
    form = RForm()
    if request.method == 'POST':
        form = RForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins')
        else:
            return HttpResponse("not working")
               
        
    context={'form':form}
    return render(request, 'loginr.html',context)


# def loginr(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#         emailw = request.POST.get('email')
#         passs = request.POST.get('password') 
#         try:
#             user = User.objects.get(email=emailw)
            
#         except:
#             messages.error(request, '{} does not exist'.format(emailw))

#         user=authenticate(request, email=emailw, password=passs)   
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'username password does not exist')

    
   
#     # return render(request,'loginr.html', context)
    
#     return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')

def events(request):
    eve_u = Events.objects.filter(status=True)
    eve_p = Events.objects.filter(status=False)
    if request.user.is_authenticated:   
        con = {'eve_u':eve_u , 'eve_p':eve_p }
    else:
        return redirect('logins')
    return render(request, 'events.html', con)

def notices(request):
    if request.user.is_authenticated:
        return render(request, 'notices.html')
    else:
        return redirect('logins')

def notes(request):
    if request.user.is_authenticated:
        return render(request, 'notes.html')
    else:
        return redirect('logins')

def qps(request):
    if request.user.is_authenticated:
        return render(request, 'qps.html')
    else:
        return redirect('logins')

def opd(request):
    if request.user.is_authenticated:
        return render(request, 'opd.html')
    else:
        return redirect('logins')

def logins(request):
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

    
   
    # return render(request,'logins.html', context)
    
    return render(request, 'logins.html')