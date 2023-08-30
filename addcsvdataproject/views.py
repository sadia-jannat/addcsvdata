from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from addcsvdataproject import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import Create
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *

# Create your views here.
def home(request):

    form=Create()
    
    if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
    context={'form':form}  
    
    return render(request, 'home.html', context)

login_result=1
def userlogin(request):
    if request.method == "POST":       
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            global login_result
            login_result=0
            
            login(request,user)

            return redirect('/') #.ata active hoise

        else:
            messages.info(request,'Username and password incorrect')
    return render(request,"userlogin.html")

def userlogout(request):
    logout(request)
    return redirect('/')

def boothadd(request):

    if request.method =="POST":
        em=booth()

        em.polling_booth_number = request.POST.get('polling_booth_number')
        em.polling_booth_name = request.POST.get('polling_booth_name')
        em.parent_constituency=request.POST.get('parent_constituency')
        em.winner_2014 = request.POST.get('winner_2014')
        em.runnerup= request.POST.get('runnerup')
        em.margin_percente=request.POST.get('margin_percente')
        em.margin = request.POST.get('margin')
        em.total_voter= request.POST.get('total_voter')
        em.bjp_votes=request.POST.get('bjp_votes')
        em.bjp_percente_votes=request.POST.get('bjp_percente_votes')
        em.inc_votes=request.POST.get('inc_votes')
        em.inc_percente_votes=request.POST.get('inc_percente_votes')
        em.winner_2019=request.POST.get('winner_2019')
        em.margin_percente_2=request.POST.get('margin_percente_2')
        em.margin_2=request.POST.get('margin_2')
        em.total_voter_2=request.POST.get('total_voter_2')
        em.bjp_votes_2=request.POST.get('bjp_votes_2')
        em.bjp_percente_votes_2=request.POST.get('bjp_percente_votes_2')
        em.inc_votes_2=request.POST.get('inc_votes_2')
        em.inc_percente_votes_2=request.POST.get('inc_percente_votes_2')
        

        em.save()

        messages.info(request,'Your data added successfully!!')
    
    return render(request, "boothadd.html", {'login_result': login_result})


def search(request):

    teamuser=TeamRegtration.objects.all()

    if request.method == 'GET':
        querynum = request.GET.get('querynum')   #variable name those three query,queryx,queryday.Not form.py query
        queryname=request.GET.get('queryname')
        queryparent=request.GET.get('queryparent')

        querywinner2014=request.GET.get('querywinner2014')
        querywinner2019=request.GET.get('querywinner2019')

        if querynum and queryname and queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result, 'teamuser':teamuser}) 
        elif querynum and queryname or queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number') 
            return render(request, 'search.html', {'products':products, 'login_result': login_result, 'teamuser':teamuser})
        elif querynum or queryname and queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number') 
            return render(request, 'search.html', {'products':products, 'login_result': login_result, 'teamuser':teamuser})
       
        elif querynum:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result, 'teamuser':teamuser}) 
        elif queryname:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result, 'teamuser':teamuser})
        elif queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result, 'teamuser':teamuser})
        elif querywinner2014:
            products = booth.objects.filter(winner_2014__icontains=querywinner2014).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result})
        elif querywinner2019:
            products = booth.objects.filter(winner_2019__icontains=querywinner2019).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result, 'teamuser':teamuser})
        
        else:
            print("No information find") 
            return render(request, 'search.html',{'login_result': login_result, 'teamuser':teamuser})     



def search_edit(request, id):
    if request.method == 'POST':
         pi=booth.objects.get(pk=id)
         fm=boothForm(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=booth.objects.get(pk=id)
           fm=boothForm(instance=pi)

    context={'fo':fm,
             'pi':pi}      
    return render(request, 'search_edit.html', {'fo':fm})    

def search_delete(request,id):
    if request.method == 'POST':
        pi=booth.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/search')

       

def dashboard(request):

    formfetch=booth.objects.all() 

    return render(request, 'dashboard.html', {'formfetch':formfetch,'login_result': login_result})

def dashboard_edit(request, id):
    if request.method == 'POST':
         pi=booth.objects.get(pk=id)
         fm=boothForm(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=booth.objects.get(pk=id)
           fm=boothForm(instance=pi)

    context={'fo':fm,
             'pi':pi}      
    return render(request, 'dashboard_edit.html', {'fo':fm})        

def dashboard_delete(request,id):
    if request.method == 'POST':
        pi=booth.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard')


def teamsignup(request):

    if request.method =="POST":
        tm=TeamRegtration()

        tm.name = request.POST.get('name')
        tm.nid= request.POST.get('nid')
        tm.location=request.POST.get('location')
        tm.email = request.POST.get('email')
        tm.password= request.POST.get('password')
        
        tm.save()

        messages.info(request,'Your signup successfully!!')

    return render(request, 'teamsignup.html')

def teamuserpage(request):
    teamuser=TeamRegtration.objects.all()
    return render(request, "teamuserpage.html", {'teamuser':teamuser} )

def teamuser_delete(request,id):
    if request.method == 'POST':
        pi=TeamRegtration.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/teamuserpage')
