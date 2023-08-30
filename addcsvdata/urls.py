"""
URL configuration for addcsvdata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from addcsvdataproject import views

#API
from addcsvdataproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('boothadd/', views.boothadd, name='boothadd'),
    path('search/', views.search, name='search'),
    path('search_edit/<int:id>/', views.search_edit, name='search_edit'),
    path('search_delete/<int:id>/', views.search_delete, name='search_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_edit/<int:id>/', views.dashboard_edit, name='dashboard_edit'),
    path('dashboard_delete/<int:id>/', views.dashboard_delete, name='dashboard_delete'),
    path('teamsignup/', views.teamsignup, name='teamsignup'),
    path('teamuserpage/', views.teamuserpage, name="teamuserpage"),
    path('teamuser_delete/<int:id>', views.teamuser_delete, name='teamuser_delete')
]
