import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#models
from .models import *
#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class boothForm(forms.ModelForm):
    class Meta:
        model=booth
        fields=['polling_booth_number','polling_booth_name', 'parent_constituency','winner_2014','runnerup','margin_percente',
                'margin','total_voter','bjp_votes','bjp_percente_votes','inc_votes','inc_percente_votes','winner_2019',
                'margin_percente_2','margin_2','total_voter_2','bjp_votes_2','bjp_percente_votes_2','inc_votes_2',
                'inc_percente_votes_2']
        

#here django create it's own model and forms
class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]