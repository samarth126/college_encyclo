from asyncore import read
from cProfile import Profile
from http.client import responses
from re import M
from urllib import response
from django.http import HttpResponseRedirect, FileResponse, Http404
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
from .models import Events,Profile,College
from django.template.loader import get_template
import os
import datetime
from django.core.files import File
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        ssu = request.user
        pro, created = Profile.objects.get_or_create(user = ssu)
        sad, created1 = Staffadmin.objects.get_or_create(user = ssu)
        staf=ssu.role
        if(staf == '1'):
            if(pro.detail_filled == False):
                return redirect('proform')
            # else:
            #     return redirect('home')
        elif(staf == '2'):
            if(sad.detail_filled_s == False):
                return redirect('staffproform')
            # else:
            #     return redirect('home')
    else:
        return redirect('logins')

    return render(request, 'home.html',{'ssu':ssu, 'staf':staf})

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

def logoutUser(request):
    logout(request)
    return redirect('home')

def events_self(request):
    eve_u = Events.objects.filter(status=True)
    eve_p = Events.objects.filter(status=False)
    clg_type = request.session['clg_type']
    if request.user.is_authenticated:   
        ssu = request.user
        staf = ssu.role
        sad = Staffadmin.objects.get(user=ssu)
        if request.method == 'POST':
            event = request.POST.get('event_s')
            date_time = request.POST.get('date_time_s')
            tg_audience = request.POST.get('tg_audience_s')
            event_desc = request.POST.get('event_desc_s')
            venue = request.POST.get('venue_s')
            eve_img1 = request.FILES.get('img1_s')
            eve_img2 = request.FILES.get('img2_s')
            eve_img3 = request.FILES.get('img3_s')
            eve_img4 = request.FILES.get('img4_s')
            s = sad.college
            events_s = Events( event=event, date_time=date_time, tg_audience=tg_audience, event_desc=event_desc, venue=venue,college=s,event_img1=eve_img1,event_img2=eve_img2,event_img3=eve_img3,event_img4=eve_img4)
            events_s.save()

        context10 = {'eve_u':eve_u, 'eve_p':eve_p, 'staf':staf, 'clg_type':clg_type}
        return render(request, 'events.html', context10)
    else:
        return render('logins')    

def events_other(request):
    eve_u = Events.objects.filter(status=True)
    eve_p = Events.objects.filter(status=False)
    clg_type = request.session['clg_type']
    if request.user.is_authenticated:   
        ssu = request.user
        staf = ssu.role
        sad = Staffadmin.objects.get(user=ssu)
        c = College.objects.all()
        if request.method == 'POST':
            event = request.POST.get('event')
            date_time = request.POST.get('date_time')
            tg_audience = request.POST.get('tg_audience')
            event_desc = request.POST.get('event_desc')
            venue = request.POST.get('venue')
            eve_img1 = request.FILES.get('img1')
            eve_img2 = request.FILES.get('img2')
            eve_img3 = request.FILES.get('img3')
            eve_img4 = request.FILES.get('img4')
            s = sad.college
            events_s = Events( event=event, date_time=date_time, tg_audience=tg_audience, event_desc=event_desc, venue=venue, college=s,event_img1=eve_img1,event_img2=eve_img2,event_img3=eve_img3,event_img4=eve_img4)
            events_s.save()

        context12 = {'eve_u':eve_u , 'eve_p':eve_p, 'staf':staf, 'c':c, 'clg_type':clg_type}
        return render(request, 'events.html', context12) 
        
    else:
        return render('logins')

def events(request):
    eve_u = Events.objects.filter(status=True)
    eve_p = Events.objects.filter(status=False)
    if request.user.is_authenticated:   
        ssu = request.user
        staf = ssu.role
        if request.method == 'POST' :
            clg_type = request.POST.get('clg_type')
            request.session['clg_type'] = clg_type
            if( clg_type == "self"):
                return redirect(events_self)
            if( clg_type == "other"):
                return redirect(events_other)
        
        context1 = {'eve_u':eve_u , 'eve_p':eve_p, 'staf':staf}
        return render(request, 'events.html', context1)
    else:
        return redirect('logins')

def notices(request):
    if request.user.is_authenticated:   
        ntc= Notice.objects.all()
        ssu = request.user
        staf = ssu.role
        sad = Staffadmin.objects.get(user=ssu)
        if request.method == 'POST' :
            notice_title = request.POST.get('notice_title')
            notice_date = request.POST.get('notice_date')
            notice_desc = request.POST.get('notice_desc')
            uploaded_file = request.FILES['filedoc']
            s = sad.college
            t = sad.department
            u = sad.year
            notices = Notice(notice_title=notice_title, notice_date=notice_date, notice_desc=notice_desc, notice_college=s, notice_dept=t, notice_year=u,notice_file=uploaded_file )
            notices.save()
        context1 = {'staf':staf, 'ntc':ntc,}
        return render(request, 'notices.html', context1)
    else:
        return redirect('logins')

def notes(request):
    if request.user.is_authenticated:
        ntc= Notes.objects.all()
        ssu = request.user
        staf = ssu.role
        oi = Subject.objects.all()
        c = College.objects.all()
        d = Department.objects.all()
        y = Year.objects.all()
        if 'modal_form' in request.POST:
            nsb = request.POST.get('nsb')
            hmm = Subject(subject=nsb)
            hmm.save()
        if 'note_form' in request.POST:
            nt_sb = request.POST.get('nt_sb')
            nt_un_no = request.POST.get('note_unit_no')
            nt_un = request.POST.get('note_unit')
            college = request.POST.get('college')
            department = request.POST.get('department')
            year = request.POST.get('year')
            nt_doc = request.POST.get('note_file')
            ehn = Subject.objects.get(id=nt_sb)
            v = College.objects.get(id=college)
            w = Department.objects.get(id=department)
            z = Year.objects.get(id=year)
            notes = Notes(notes_subject=ehn, notes_unit_no=nt_un_no, notes_unit=nt_un, notes_college=v, notes_dept=w, notes_year=z, notes_file=nt_doc)
            notes.save()
        context = {'staf':staf, 'oi':oi, 'c':c, 'd':d, 'y':y, 'ntc':ntc} 
        return render(request, 'notes.html', context)
    else:
        return redirect('logins')

def subnotes(request, pk):
    if request.user.is_authenticated:
        nt = Notes.objects.filter(notes_subject=pk)
        context = {'nt':nt}
        return render(request, 'subnotes.html', context)
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