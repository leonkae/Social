from django import forms
import django
from django.forms import CharField, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        