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

def search(request):

    if request.method == 'GET':
        querynum = request.GET.get('querynum')   #variable name those three query,queryx,queryday.Not form.py query
        queryname=request.GET.get('queryname')
        queryparent=request.GET.get('queryparent')

        if querynum and queryname and queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result}) 
        elif querynum and queryname or queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number') 
            return render(request, 'search.html', {'products':products, 'login_result': login_result})
        elif querynum or queryname and queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number') 
            return render(request, 'search.html', {'products':products, 'login_result': login_result})
       
        elif querynum:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result}) 
        elif queryname:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result})
        elif queryparent:
            products = booth.objects.filter(polling_booth_number__icontains=querynum, polling_booth_name__icontains=queryname, parent_constituency__icontains=queryparent).order_by('polling_booth_number')
            return render(request, 'search.html',{'products':products, 'login_result': login_result})
        else:
            print("No information find") 
            return render(request, 'search.html',{'login_result': login_result})     



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
