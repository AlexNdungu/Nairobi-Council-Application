from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets     




#Below here are the upload froms

from .models import *

#Below are th edjangof forms

#This Is the user register form

class createUserForm(UserCreationForm):

    password2 = None

    class Meta:
        model = User
        fields = ['username','email','password1']
        

#Personal information form

class appplicantInfoForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['user']

#Next Of Kin form

class NextOfKinForm(forms.ModelForm):

    class Meta:
        model = Next
        fields = '__all__'       
        exclude = ['user']


#Educational Background form

class UniversityForm(forms.ModelForm):

    class Meta:
        model = Higher
        fields = '__all__'     
        exclude = ['user']
  

#SecondaryForm Background form

class SecondaryForm(forms.ModelForm):

    class Meta:
        model = Secondary 
        fields = '__all__'   
        exclude = ['user']

#Primary_Education Background form

class PrimaryForm(forms.ModelForm):

    class Meta:
        model = Primary
        fields = '__all__'        
        exclude = ['user']
        
#Upload Files

class upFilesAll(forms.ModelForm):

    class Meta:
        model = Upload
        fields = '__all__' 
        exclude = ['user']
    